// Server Chat
#include <sys/socket.h>

#include <netinet/in.h>

#include <sys/types.h>

#include <arpa/inet.h>

#include <stdio.h>

#include <stdlib.h>

#include <string.h>

struct sockaddr_in serv_addr, cli_addr;

char serv_ip[] = "127.0.0.1";

unsigned int serv_port = 25000;

int sock, b, l, len, a, rd, w;

char buff[128];

char buff1[128];

int main()
{

    sock = socket(AF_INET, SOCK_STREAM, 0);

    if (sock < 0)
    {

        printf("Socket not connected\n");

        exit(0);
    }

    serv_addr.sin_family = AF_INET;

    serv_addr.sin_port = htons(serv_port);

    inet_aton(serv_ip, &(serv_addr.sin_addr));

    b = bind(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

    if (b < 0)
    {

        printf("Bind not done\n");

        close(sock);

        exit(0);
    }

    l = listen(sock, 7);

    if (l < 0)
    {

        printf("Server Error\n");

        close(sock);

        exit(0);
    }

    len = sizeof(cli_addr);

    a = accept(sock, (struct sockaddr *)&cli_addr, &len);

    if (a < 0)
    {

        printf("Cannot accept\n");

        close(sock);

        exit(0);
    }

    for (;;) // Infinite Loop

    {

        rd = read(a, buff, 128);

        if (rd < 0)
        {

            printf("Cannot receive message");
        }

        else

        {

            puts(buff);

            if (strcmp("bye", buff) == 0)

                break;

            buff[rd] = '\0';

            printf("\nClient: %s\n", buff);

            gets(buff1);

            w = write(a, buff1, 128);

            /*puts(buff);

            if(strcmp("bye", buff)==0)

                break;*/

            if (w < 0)

                printf("Error in write\n");

            else

                printf("Server echoed back\n");
        }
    }
}
