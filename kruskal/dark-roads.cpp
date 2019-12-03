#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

#define scanner2(m, n) scanf("%d%d", &m, &n)
#define scanner3(x, y, z) scanf("%d%d%d", &x, &y, &z)
struct Edge { int x, y, z; };

int amount;
int vertices[999999];
Edge edges[999999];

// Creating individual sets
void makeSet(int n) {
    for (int i = 0; i < n; i++)
        vertices[i] = i;
}

// Getting the sets created
int findSet(int n) {
    if(vertices[n] != n)
        vertices[n] = findSet(vertices[n]);
    return vertices[n];
}

// Union of sets
int unionSet(int x, int y, int p) {
    int i = findSet(x), j = findSet(y);

    if(i != j) {
        amount -= edges[p].z;
        if(i > j) vertices[i] = j;
        else vertices[j] = i;
        return 1;
    }

    return 0;
}

// (a,b) => a.z - b.z
int compare(const void *a, const void *b) {
    return (*(struct Edge *)a).z - (*(struct Edge *)b).z;
}

int main(int argc, char const *argv[]) {
    int m, n, i;

    while(scanner2(m, n) && (m || n)) {
        amount = 0;
        memset(&edges, 0, sizeof(edges));

        for (i = 0; i < n; i++) {
            scanner3(edges[i].x, edges[i].y, edges[i].z);
            amount += edges[i].z;
        }

        makeSet(m);
        qsort(edges, n, sizeof(edges[0]), compare);
        for (i = 0; i < n; ++i)
            unionSet(edges[i].x, edges[i].y, i);
        printf("%d\n", amount);
    }

    return 0;
}