## Python graph

```
    BFS(G, s)
for each vertex u ∊ G.V - {s}
    u.color = WHITE
    u.d = ∞
    u.π = None
s.color = 0
s.π = None
Q=0
Enqueue(Q, s)
while Q ≠ 0
    u = Dequeue(Q)
    for each v ∊ G.adj[u]
        if v.color is WHITE
            v.color = GRAY
            v.d = u.d + 1
            v.π = u
            Enqueue(Q, v)
        u.color = BLACK
```
>### Analiza BFS

Predpostavimo da imamo graf od V cvorova i E ivica. Nakon inicijalizacije BFS nikad ne izbeljuje cvor, tako da garantuje da ce se scaki cvar bar jednom staviti u red cekanja i isto tako bar jednom ukloniti iz reda.

Operacija stavljanja i skidanja sa reda je O(1). Tako da ukupno vreme cekanja je O(V), jer procedura prati listu ivica za svaki cvor samo kada se ivica skida sa reda cekanja, prati svaku listu barem jednom sa obzirom da je suma svih ivica Θ(E). Ukupno vreme potroseno u proveravanju lista O(E). Ukupna inicializacija O(V) i ukupno vreme izvrsenja BFS-a je O(V + E).

Tako da se BFS izvrsava u linearnom vremenu velicine liste ivica

```
    DFS(G)
for each vertex u ∊ G.V
    u.color = WHITE
    u.π = None
time = 0
for each vertex u ∊ G.V
    if u.color == WHITE
        DFS-visit(G, u)

    DFS-visit(G, u)
time = time + 1
u.d = time
u.color = GRAY
for each v ∊ G.adj[u]
    if v.color == WHITE
        v.π = u
        DFS-visit(G, v)
u.color = BLACK
time = time + 1
u.f = time
```
>### Analiza DFS
Pretpostavimo da je graf povezan. DFS posecuje svaki cvor u grafu i proverava svaku njegovu ivicu. Stoga vremenska kompleksnost je O(V+E). Ukoliko se koristi matrica suseda za reprezentaciju grafa ne mogu sve ivice jednog cvora efikasno prikazati sto resultuje kompleknost O(V<sup>2</sup>)

Stefan Nićetin RA188-2014 \
Srđan Šuvakov RA174-2014 \
Luka Ercegovčević RA165-2014 \
Milan Vuletić RA131-2013 \
Maksim Egelja RA51-2014 \
Milan Vidić RA241-2015
