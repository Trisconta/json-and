
## SED hints
```text
sed -E 's/"/~/g; s/^/"/; s/\t/","/g; s/$/"/' ref_plays.tsv
"#PID","ID","Name"
"P110","15011205223","Gold Ballads And Candies, Slow Rock"
"P111","15010527903","Keep You Waiting Now"
"P112","15029708863","Oh Papa Do You Preach"
"P113","15058630203","Sprouts and Appetizers"
"P114","15081458643","Say You Were At The ~80s~ Right?"
"P115","15083071583","Turn Back The Clock"
```

Now, subtle improvement, if input line starts with a hash symbol ('#'), do not substitute:
1. `sed -E '/^#/! s/"/~/g; /^#/! s/^/"/; /^#/! s/\t/","/g; /^#/! s/$/"/' ref_plays.tsv`
