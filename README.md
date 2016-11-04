# Installation
Project utilizes docker containers, so no installation required, but you still need docker, which you probably already have anyways

# Usage
To build & run project, execute `./pokehelper.sh <email> <command>`, where email
is your google email (PTC accounts are not supported), and command is one of:

* `rename` — renames your pokemons to meaningful nicknames like 42A15D14S135, which is
[Sum IV]A[Attack IV]D[Defence IV]S[Stamina IV][Kilometers to walk with buddy]. Learn more about IV at https://pokeassistant.com/main/ivcalculator
* `analyze_xp` — analyzes how much pokemons you can evolve right now with a Pidgey spam technique. Based on https://pokeassistant.com/main/pidgeyspam
