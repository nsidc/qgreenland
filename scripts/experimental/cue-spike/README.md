# Installation

Install cue and make CLI available:

    apt install golang-go
    GO111MODULE=on go get cuelang.org/go/cmd/cue
    alias cue=~/go/bin/cue


NOTE: The alias set above expires with your session. Consider adding it to your
`.bashrc`


# Usage

    cue eval -c new_cfg/config.cue

The `-c` flag is for "concrete", meaning definitions (`#Foo`) are excluded from
the output.
