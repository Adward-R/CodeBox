//server
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/fcntl.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <time.h>

#define BUF_SIZE 4096 //block transfer size
#define QUEUE_SIZE 10
#define DEFAULT_PORT 12345
#define MAX_PORTS 10

int sa; //default socket of server
char shared; //shared memory in SEND
//int thread_pool[MAX_PORTS]; //1 for using

struct {
    int using; //1 for using
    struct hostent *h;
    int s; //socket
    int ns; //non-block socket
    int in_critical;
    int send_target;
    int send_src;
} thread_pool[MAX_PORTS];

struct thread_param{
    int i;
    struct sockaddr_in peer_addr;
    socklen_t addr_len;
};

/*fatal(char *string) {
    printf("%s\n", string);
    exit(1);
}

void server_thread_esc() {
    
}*/
void get_sys_time(char *buf) {
    time_t t = time(0);
    strftime(buf, BUF_SIZE, "%Y/%m/%d %X %A %z",localtime(&t));
}

void listen_thread(int *arg) {
    int self = *arg;
    int bytes;
    char ch;
    printf("Daemon started\n");
    while (thread_pool[self].using) {
        if (thread_pool[self].send_src) {
            //printf("conn %d be set as send src\n", self);
            if (!shared) {
                if ((bytes = read(thread_pool[self].ns, &ch, 2))>=0) {
                    shared = ch;
                    if (ch=='\n') { //end of message
                        thread_pool[self].send_src = 0;
                    }
                    //read(thread_pool[self].ns, &shared, 2);
                    //printf("shared= %c\n", shared);
                }
            }

        }
        //if (thread_pool[self].in_critical) {
        //    usleep(30000);
        //    continue;
        //}
        if (thread_pool[self].send_target) {
            //printf("conn %d be set as send target\n", self);
            if (shared) { //has anything to read
                if (shared!='\n') {
                    write(thread_pool[self].ns, &shared, 2);
                }
                else {
                    thread_pool[self].send_target = 0;
                }
                shared = 0;
            }
        }
    }
    printf("listen_thread exiting...\n");
    pthread_exit(0);
}

void server_thread(struct thread_param *arg) {
    int self = arg->i;
    int i, j, c, bytes;
    char buf[BUF_SIZE], tmp[BUF_SIZE];
    char ch;
    struct sockaddr_in channel; //holds IP address
    pthread_t send_and_listen;

    printf("thread num (self) %d\n", self);
    
    thread_pool[self].h = gethostbyaddr(&(arg->peer_addr).sin_addr, sizeof((arg->peer_addr).sin_addr), AF_INET);
    if (thread_pool[self].h < 0) {
        printf("gethostbyaddr failed\n");
        //close(sa);
        thread_pool[self].using = 0;
        pthread_exit(1);
    }
    
    thread_pool[self].s = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (thread_pool[self].s < 0) {
        printf("socket failed\n");
        //close(sa);
        thread_pool[self].using = 0;
        pthread_exit(1);
    }
    
    memset(&channel, 0, sizeof(channel));
    channel.sin_family = AF_INET;
    memcpy(&channel.sin_addr.s_addr,
           (thread_pool[self].h)->h_addr,
           (thread_pool[self].h)->h_length);
    
    //connect back to client on default port 12346
    channel.sin_port = htons(DEFAULT_PORT + 1 + self);
    c = connect(thread_pool[self].s, (struct sockaddr *)&channel, sizeof(channel));
    if (c < 0) {
        printf("connect client failed with exit code 0\n");
        //close(sa);
        thread_pool[self].using = 0;
        pthread_exit(1);
    }
    
    //connect back to client on non-block default port 12344
    channel.sin_port = htons(DEFAULT_PORT - 1 - self);
    thread_pool[self].ns = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    //fcntl(thread_pool[self].ns, F_SETFL, O_NONBLOCK); //set non-blocked socket
    c = connect(thread_pool[self].ns, (struct sockaddr *)&channel, sizeof(channel));
    if (c < 0) {
        printf("connect client failed with exit code 1\n");
        //close(sa);
        thread_pool[self].using = 0;
        pthread_exit(1);
    }
    //close(sa);
    printf("Connection established!\n");
    //Real connection to client established
    
    //create a new thread to transfer buffered char
    pthread_create(&send_and_listen, NULL, (void *)listen_thread, &self);
    
    while (1) {
        thread_pool[self].in_critical = 0;
        bytes = read(thread_pool[self].s, buf, BUF_SIZE); //get cmd from client
        thread_pool[self].in_critical = 1;
        //printf("%d\n", bytes);
        if (bytes <= 0) {
            continue;
        }
        else if (!strcmp(buf, "DISC")) {
            close(thread_pool[self].s);
            printf("Client disconnected\n");
            thread_pool[self].using = 0;
            pthread_exit(0);
        }
        else if (!strcmp(buf, "TIME")) {
            memset(buf, 0, sizeof(buf));
            get_sys_time(buf);
            write(thread_pool[self].s, buf, sizeof(buf));
        }
        else if (!strcmp(buf, "NAME")) {
            memset(buf, 0, sizeof(buf));
            if (!gethostname(buf, BUF_SIZE)) {
                write(thread_pool[self].s, buf, sizeof(buf));
            }
            else {
                printf("Get hostname error\n");
                continue;
            }
        }
        else if (!strcmp(buf, "LIST")) {
            memset(buf, 0, sizeof(buf));

            for (i=0; i<MAX_PORTS; i++) {
                if (thread_pool[i].using) {
                    //printf("Num %d in use...\n", i);
                    memset(tmp, 0, sizeof(tmp));
                    //sprintf(tmp, "%d", i);
                    buf[0] = '\n';
                    buf[1] = (char)(i+'0');
                    buf[2] = '\t';
                    memset(tmp, 0, sizeof(buf));
                    /*for (pptr=(thread_pool[i].h)->h_addr_list;
                         pptr!=NULL; pptr++) {
                        write(s, inet_ntop((thread_pool[i].h)->h_addrtype, *pptr, buf, sizeof(buf)), sizeof(buf));
                    }*/
                    inet_ntop((thread_pool[i].h)->h_addrtype,
                              *(thread_pool[i].h)->h_addr_list,
                              tmp, sizeof(tmp));
                    memcpy(buf+3, tmp, BUF_SIZE-3);
                    write(thread_pool[self].s, buf, BUF_SIZE);
                }
                else {
                    write(thread_pool[self].s, "NONE", BUF_SIZE);
                }
            }
           
        }
        else if (!strcmp(buf, "SEND")) {
            write(thread_pool[self].s, "PARAM", 6);
            read(thread_pool[self].s, &ch, 2);
            i = ch - '0';
            if (thread_pool[i].using) {
                shared = 0;
                thread_pool[self].send_src = 1;
                thread_pool[i].send_target = 1;
            }
            else {
                printf("Inactive client num!\n");
                continue;
            }
        }
        else {
            continue;
        }
        
    }
    
    
    
    
    
}

int main(){
    pthread_t tasks[MAX_PORTS];
    
    int s, b, l, fd, bytes, on = 1;
    int i, j;
    char buf[BUF_SIZE]; //buffer for outgoing file
    struct sockaddr_in channel; //holds IP address
    
    struct thread_param params;
    memset(&params, 0, sizeof(params));
    memset(thread_pool, 0, sizeof(thread_pool));
    
    //Build address structure to bind to socket.
    memset(&channel, 0, sizeof(channel));
    channel.sin_family = AF_INET;
    channel.sin_addr.s_addr = htons(INADDR_ANY);
    channel.sin_port = htons(DEFAULT_PORT);
    
    //Passive open. Wait for connection.
    s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP); //create socket
    if (s < 0) {
        printf("socket failed\n");
        exit(1);
    }
    setsockopt(s, SOL_SOCKET, SO_REUSEADDR, (char *)&on, sizeof(on));
    b = bind(s, (struct sockaddr *)&channel, sizeof(channel));
    if (b < 0) {
        printf("bind failed\n");
        exit(1);
    }
    
    l = listen(s, QUEUE_SIZE); //specify queue size
    if (l < 0) {
        printf("listen failed\n");
        exit(1);
    }
    
    /* Socket is now set up and bound. Wait for connection and process it. */
    while (1) {
        sa = accept(s, 0, 0); //block for connection request
        if (sa < 0) {
            printf("accept failed\n");
            close(sa);
            continue;
        }
        params.addr_len = BUF_SIZE; //sizeof(params.peer_addr);
        if (getpeername(sa, (struct sockaddr *) &(params.peer_addr), &(params.addr_len)) < 0) {
            printf("Get client address failed\n");
            close(sa);
            continue;
        }
        close(sa); //
        i = 0;
        while (thread_pool[i].using){ i++; }
        params.i = i;
        thread_pool[i].using = 1;
        pthread_create(&tasks[i], NULL, (void *)server_thread, &params);
    }
    
    
    
    return 0;
}
