//client
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <string.h>

#define BUF_SIZE 4096 //block transfer size
#define QUEUE_SIZE 10
#define DEFAULT_PORT 12345
#define CLIENT_PORT 12346
#define MAX_PORTS 10

/* 
    CONN
    DISC
    TIME
    NAME
    LIST
    SEND
    QUIT
*/

void fatal() {
    printf("Usage: ...\n");
    printf(">>> ");
}

int sa;

void listen_thread(void *arg) {
    char ch;
    printf("thread started\n");
    while (1) {
        read(sa, &ch, 2);
        write(1, &ch, 2);
//        usleep(30000);
    }
}

int main() {
	int i, j, c, s, _s, b, l, bytes, on = 1, isBinded = 0;
	char buf[BUF_SIZE]; //buffer for incoming file
    char ch;
	struct hostent *h = NULL; //info about server
	struct sockaddr_in channel; //holds IP address
    pthread_t send_and_listen;
    //init
    
    char cmd[10];
    char param[BUF_SIZE];
    //int port;
    int scan_num;
    
    while (1) {
        printf(">>> ");
        scanf("%s", cmd);
        if (!strcmp(cmd, "disconn")) {
            write(sa, "DISC", 5);
            close(sa);
            printf("Disconnected from remote\n");
        }
        else if (!strcmp(cmd, "time")) {
            write(sa, "TIME", 5);
            bytes = read(sa, buf, BUF_SIZE);
            if (bytes <= 0) {
                printf("Get server time failed\n");
                continue;
            }
            write(1, buf, bytes);
            printf("\n");
        }
        else if (!strcmp(cmd, "name")) {
            write(sa, "NAME", 5);
            bytes = read(sa, buf, BUF_SIZE);
            if (bytes <= 0) {
                printf("Get server name failed\n");
                continue;
            }
            write(1, buf, bytes);
            printf("\n");
        }
        else if (!strcmp(cmd, "list")) {
            write(sa, "LIST", 5);
            for (i=0; i<MAX_PORTS; i++) {
                bytes = read(sa, buf, BUF_SIZE);
                if (strcmp(buf, "NONE")) {
                    write(1, buf, bytes);
                }
            }
            printf("\n");
        }
        else if (!strcmp(cmd, "quit")) {
            write(sa, "DISC", 5);
            close(sa);
            printf("Disconnected from remote\n");
            printf("Quitting...\n");
            exit(0);
        }
        else if (!strcmp(cmd, "conn")) {
            scanf("%s", param);
            h = gethostbyname(param); //look up host's IP address
            if (!h) printf("gethostbyname failed\n>>> ");
            
            s = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
            if (s < 0) printf("socket failed\n>>> ");
            
            memset(&channel, 0, sizeof(channel));
            channel.sin_family = AF_INET;
            memcpy(&channel.sin_addr.s_addr, h->h_addr, h->h_length);
            
            //link to default port
            channel.sin_port = htons(DEFAULT_PORT);
            c = connect(s, (struct sockaddr *) &channel, sizeof(channel));
            if (c < 0) {
                printf("connect failed with exit code 1\n>>> ");
                exit(1);
            }

            //bind the client port
            if (!isBinded) {
                //block to wait for the server to connect back
                channel.sin_addr.s_addr = htons(INADDR_ANY);
                _s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
                if (_s < 0) printf("socket failed\n>>> ");
                
                setsockopt(_s, SOL_SOCKET, SO_REUSEADDR, (char *)&on, sizeof(on));

                channel.sin_port = htons(DEFAULT_PORT + 1);
                b = bind(_s, (struct socketaddr *)&channel, sizeof(channel));
                if (b < 0) {
                    printf("bind failed\n");
                    exit(1);
                }
                
                l = listen(_s, QUEUE_SIZE); //specify queue size
                if (l < 0) {
                    printf("listen failed\n");
                    exit(1);
                }
                
                isBinded = 1;
            }
            //
            
            sa = accept(_s, 0, 0); //block for server's connecting back
            if (sa < 0) {
                printf("accept failed\n");
                exit(1);
            }
            close(s); //end previous session on client voluntarily
            
            /* Socket is now set up and bound. Wait for connection and process it. */
            
            //real connection established on "sa"
            printf("Connection established!\n");
            pthread_create(&send_and_listen, NULL, (void *)listen_thread, NULL);
        }
        else if (!strcmp(cmd, "send")) {
            scanf("%s", param);
            write(sa, "SEND", 5);
            memset(buf, 0, BUF_SIZE);
            read(sa, buf, BUF_SIZE);
            if (strcmp(buf, "PARAM")) {
                printf("send cmd error\n");
                continue;
            }
            write(sa, param, sizeof(param));
            printf("You can now send message to client no.%s, end with ENTER :\n", param);
            while ((ch=getchar())!='\n') {
                write(sa, &ch, 2);
            }
        }
        else {
            fatal();
        }
    }

    return 0;
}
