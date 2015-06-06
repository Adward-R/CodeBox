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
#define CLIENT_PORT 12346

int sa;
int thread_pool[MAX_PORTS]; //1 for using

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

void server_thread(struct thread_param *arg) {
    int i, j, c, s, bytes;
    char buf[BUF_SIZE]; //buffer for incoming file
    struct sockaddr_in channel; //holds IP address
    
//    struct hostent *h = gethostbyname((arg->peer_addr).sin_addr.s_addr);
    struct hostent *h = gethostbyname("localhost");
    if (h < 0) {
        printf("gethostbyname failed\n");
        //close(sa);
        thread_pool[arg->i] = 0;
        pthread_exit(1);
    }
    
    s = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (s < 0) {
        printf("socket failed\n");
        //close(sa);
        thread_pool[arg->i] = 0;
        pthread_exit(1);
    }
    
    memset(&channel, 0, sizeof(channel));
    channel.sin_family = AF_INET;
    memcpy(&channel.sin_addr.s_addr, h->h_addr, h->h_length);
    
    //connect back to client on one of default ports
    i = 0;
    do {
        i++;
        channel.sin_port = htons(DEFAULT_PORT + i); //start from 12346
        c = connect(s, (struct sockaddr *)&channel, sizeof(channel));
    } while (c < 0 && i <= 5);
    if (c < 0) {
        printf("connect client failed\n");
        //close(sa);
        thread_pool[arg->i] = 0;
        pthread_exit(1);
    }
    //close(sa);
    printf("Connection established!\n");
    //Real connection to client established
    while (1) {
        bytes = read(s, buf, BUF_SIZE); //get cmd from client
        //printf("%d\n", bytes);
        if (bytes <= 0) {
            continue;
        }
        else if (!strcmp(buf, "DISC")) {
            //close(s);
            printf("Client disconnected\n");
            thread_pool[arg->i] = 0;
            pthread_exit(0);
        }
        else if (!strcmp(buf, "TIME")) {
            memset(buf, 0, sizeof(buf));
            get_sys_time(buf);
            write(s, buf, sizeof(buf));
        }
        else if (!strcmp(buf, "NAME")) {
            memset(buf, 0, sizeof(buf));
            if (!gethostname(buf, BUF_SIZE)) {
                write(s, buf, sizeof(buf));
            }
            else {
                printf("Get hostname error\n");
                continue;
            }
        }
        else if (!strcmp(buf, "LIST")) {
            //
        }
        else if (!strcmp(buf, "SEND")) {
            //
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
        /*params.addr_len = sizeof(params.peer_addr);
        if (getpeername(sa, (struct sockaddr *) &(params.peer_addr), &(params.addr_len)) < 0) {
            printf("Get client address failed\n");
            close(sa);
            continue;
        }*/
        close(sa); //
        i = 0;
        while (thread_pool[i]){ i++; }
        params.i = i;
        pthread_create(&tasks[i], NULL, (void *)server_thread, &params);
        thread_pool[i] = 1;
    }
    
    
    
    return 0;
}
