#include <stdio.h>
#include <stdlib.h>

struct Board
{
    int width, height;
    char *data;

    char &light(int i, int j)
    {
        return data[i + width*j];
    }

    void print()
    {
        for(int j = 0; j < height; j++)
        {
            for(int i = 0; i < width; i++)
                printf("%d ", light(i,j));
            printf("\n");
        }
        printf("\n");
    }

    void clear()
    {
        for(int i = 0; i < width; i++)
            for(int j = 0; j < height; j++)
                light(i,j) = 0;
    }

    Board(int W, int H)
    {
        if(W < 0) exit(1);
        if(H < 0) exit(1);
        width = W;
        height = H;

        data = new char[width*height];

        clear();
    }

    ~Board()
    {
        delete[] data;
    }

    void chg(int i, int j)
    {
        if(i >= 0 && i < width)
            if(j >= 0 && j < height)
                light(i,j) = 1 ^ light(i,j);
    }

    void click(int i, int j)
    {
        chg(i, j);
        chg(i+1, j);
        chg(i-1, j);
        chg(i, j+1);
        chg(i, j-1);
    }
};

bool verify(int width, int height)
{
    Board board(width, height);
    Board matrix(width, width);

    bool fail = false;

    for(int p = 0; p < width; p++)
    {
        board.clear();
        board.click(p,0);

        for(int j = 1; j < height; j++)
            for(int i = 0; i < width; i++)
                if(board.light(i,j-1) == 1)
                    board.click(i,j);

        for(int i = 0; i < width; i++)
            matrix.light(i,p) = board.light(i,height-1);
    }

    for(int i = 0; i < width; i++)
    {
        bool has_pivot = false;
        for(int p = i; p < width; p++)
        {
            if(matrix.light(i,p) == 0) continue;
            has_pivot = true;

            for(int k = i; k < width; k++)
            {
                char c = matrix.light(k,p);
                matrix.light(k,p) = matrix.light(k,i);
                matrix.light(k,i) = c;
            }

            break;
        }

        if(!has_pivot) fail = true;;

        for(int j = i+1; j < width; j++)
        {
            if(matrix.light(i,j) == 0) continue;
            for(int k = i; k < width; k++)
                matrix.light(k, j) ^= matrix.light(k, i);
        }
    }

    //if(fail) printf("%d x %d failed!\n", width, height);
    //else printf("%d x %d succeded!\n", width, height);

    return !fail;
}

int main()
{
    printf("Works for...\n");
    for(int s = 1; s < 300; s++)
    {
        if(verify(s,s)) printf("%d\n", s);
    }
    return 0;
}
