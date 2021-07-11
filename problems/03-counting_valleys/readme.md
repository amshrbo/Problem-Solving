### Problem info
- website: HackeRank
- Name: counting valleys
- Difcullty: easy

### Probelm describiton
- Describtion:
    - Given a string contains of 'U and D' chars as U for clibming Up to the hill and D goes down the hill
    - The hike through a valley achived when we goes down hill then goes back to the sea level.
    = Caculate how many valleies traversed in a given path [UDUUUDUUUUDUD]
    - e.g, `strings = [UDDDUDUU] that we return a 1 as we go through a single valley.

- Input: 
    - `steps` an integer that show the nubmer of steps
    - `path` a string consits of chars 'U' and 'D' for showing the path of the hiking

### My solution
- It is a simply if and else chk for manpulating the sea level based on the U or D on the path by increasing or decreasing 1 from it.
- If the sea level comes to zero and the The char is `U` then we made a hike through a valley
- keep counting until we reach the end of the path.
