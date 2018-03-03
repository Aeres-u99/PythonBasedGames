import random
Licensing = ''' All these Ascii art images are obtained from Internet and various sources which probably had no copy-paste restrictions as such,
                In case of any dispute/violation the art in topic shall be removed spontaneously without ado
                You are free to use the code to your purpose , only requirement is that this License string is not removed and a method must be provided to print it

                Created by :- Akuma
            '''
def Game(name):
    player = name
    tease = [''' \
                
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
            ''']
    smiley = [''' \
                     __ooooooooo__
                 oOOOOOOOOOOOOOOOOOOOOOo
             oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
          oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
     oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
    oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
    oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
   oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
   oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
   oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
    *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
    *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
     *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
      *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
        *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
          *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      A heart at peace
             *OOOOOOOOo           oOOOOOOOO*      gives life to the body.
                 *OOOOOOOOOOOOOOOOOOOOO*                    ~ Akuma
                      ""ooooooooo""


            ''']    
    
    print("The game we are going to play is really easy, I will choose a number and you will have to guess it within 5 attempts")
    print("Ahh and also I will guess the numbers based on your choice of difficulty :p")
    while(1):
        print("\tHow difficult do you want it?,"+player+" [Dummy/Easy/Medium/Hard/Impossible/Insane!]")
        difficulty = input("[Difficulty]~ ")
        if difficulty == 'Dummy' or difficulty == 'dummy':
            level = 20
            break
        elif difficulty == 'Easy' or difficulty == 'easy':
            level = 40
            break
        elif difficulty == 'Medium' or difficulty == 'medium':
            level = 50
            break
        elif difficulty == 'Hard' or difficulty == 'hard':
            level = 100
            break
        elif difficulty == 'Impossible' or difficulty == 'impossible':
            level = 1000
            break
        elif difficulty == 'Insane' or difficulty == 'insane':
            level = 10000
            break
        else:
            print("ehhhh that level of difficulty does not exist!!, Try again b-baka!")
    print("hmm Nice, you want to play with",difficulty," Nice choice!")
    print("I will guess a number between 1 to ",level)
    ScarletGuess = random.randint(1,level)
    attempt = 0
    while(attempt <=6):
        if(attempt == 5 and PlayerGuess != ScarletGuess):
            print("Well you lost :( ")
            print(tease[0])
            print("Nevermind better luck next time!")
            print("By the way my guess was",ScarletGuess)
            print("Want to play again ?, trust me it was fun!")
            break
        print("Okay guess the number :D")
        attempt +=1
        print("You have ",(6-attempt)," attempts left!")
        PlayerGuess = int(input("[]:~  "))
        if PlayerGuess < ScarletGuess:
            print("Stupid, thats way toooo low!")
        elif PlayerGuess > ScarletGuess:
            print("Thats way tooo large baka!")
        elif PlayerGuess == ScarletGuess:
            print("Whoa! nice well played")
            print("That too in ",attempt,"attempts")
            print(smiley[0])
            print("Well Done!, wanna play again? ")
            break
        else:
            print("Strange this should not happen oopsie I forgot the number, I am sorry ;_; ")
            print("Hyouka..., guess what I want Akuma-sama to treat me with a cup of coffee and Icecream")
    return 

##############################################################################################        
girl =[""" \ 
                       "$
                       $"                            '#$
                      P                                  "*$
                    $"                                      '#
                   $"                                        '+'R
                  $"                  :                      < ^o"
                 $"                ~ x"                       "u N#
                $"               z" dF x$   $                  ^k'U
               $"              n4 ."# d$   d$   >               $ $
              $"        u"   ?  .u/ <%'"  d$$  u x              9 $
             $"         .o %'$@ $$  L3" u$$$~ d"x$         r4   $     
             F         ''  @H@" "'.z$e@$$$$"x* -"\r     W  E4  :$
            F           #- JMM$u. @$$$$$$$$$z$ 4 .      R :"$ .$
           F              "?MMMR$$$$$$$$$$$ #h.$#     .$" Pd$z
          F                 RMMM$$$$$$$XMf$. '$$"     9F.$
         P                   MMM$$$$L ""N@$$$$$       4d$
        $                  .x *MM$$$$*$$$$$$$*        '$
       $                   $RH.`M$$$$$$$$$$*           $
      $                   :MM$$b "$$$$*""              $
     $                    $MM$$$$8W-                   4
    $                    '$MMM$$$$$      ..             $
   $                       ^*M$$$$$?.     `~~~ ee.      $
  $"                        !.*$$$$$$k         $$$b     '$
 $"    .eu.                  `!'#**7CU         9$**$o    R
 F    @$B*".e.                 `-"$$$$B      ...uC?*MI    $
P    dP"ud$$$WXL                   R$$$   ""#*R$beUJ9$$.  `$
     Ldt$$$l$$$#c                   "$$        *uJC$$$$$N. #$
    @$L$$l$$$Pbc$                     R      ud*"?"*MM$$$$e #$
    $$$G$$$$l$$" z!x                           #$$$$u*MR$$$$b2$
   @$T@$$$T@$* u!$@M$L                        ^*^$$$$$(MMR$$$$N
  :#d$$$#d$P".$$LF$X$Rb.               J$L      ''$$$$$*J#MM$$$E
  )$$$*z$$".@$$$B:$$$$$$$c...ur        $$$.      d:$$#z$$$4RM$$$'
 x$$$)$$" d$$$$$$$$$$BR$$$$$$"        $$$$$:    :$$ $$$$#00RM$$$>
 eI#@$* d$$$$$$$*t$$$$$$$$$$$L       d$$$$$$L   $$$N$$#o$Lt8M$$$b  
 $T$$"zW@IBbW$$$$3$$$$$$$$$$$$$N    d$$$$$$$$o d9$$FuH$$$EMMM$$$$   
  "* $$$$$$$$$**#M$$$$$$$$R$$$$$$u d$$$$$$$$$$$$H2h4MM$$$F$RM$$$$    
    $$We(?Lx.  ~M$W*$$$$8$$$$$$$$$$$$$$M)W$$#d$RX$ XRM$$$>MRM$$$$L    
    $$$$$MM$X   ~$$N"$R$$$$$$$$$` '$$$T@$$$X$*"@$" XMMM$$ MMMM$$$$    
    $$$$$BM@R    "$$$7$X$$$$$$$$   $T@$$RM@$$  <"  !$MMM$'R@MM$$$$    
    $$$$$$MRR      $$$$$x$$$$$$$$eMo$$$$X$$$Tuu^   'BMMM$tMMMM$$$$L   
    $$$$$$MMR      %$$$$$k$$$$$$RX$$$$$$$$8W$$F     #$MMf8MMMM$$$$$   
    $$$$$$MM$      $$$$$$$k$$$$l$$$$$$$$$$$$$$       $MM>RMMMM$$$$$.  
    $$$$$$$M$     J$$*$$$$$iR$$$$$$$$$$$$$$$$M        $M>MMMM$$$$$$$  
    $$$$$$$$5k   .$$$9WeeWWWoeWe@$$$N$$$$$$$$k         $XMMMH$$$$$$$  
    $$$$$$$$$$c .$$BRBbebUUWUUCC$$$$$$$$$$$$$$         '$LMMM$$$$$$P
     $$$$$$$$$B.$$$$$$$$$$$$$$$*#$$$$$$$$$$$":"          $8MM$$$$$$
     'MR$$$$$$$8`$$$$M$$$$$$$$F  4$$$$$$$$$$.`~k          "NMM$$$$
      #MMR$$$$$$k$$$$B$$$$$$$$$oz$$$$$$$$$$$$N$$c           ^N$$#
       $MMM$$$$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$c
       '$MMR$$$$$N?$$5$$$$$$$$$$$$$$$$$$$$$$$$$$$$c
        `@MMR$$$$$k$B$R$$$$$$$$$$$$$$$$$$$$$$$$$$$$b
         #@MMR$$$$$'#R$$$$$$$$$$$$$$$$$$R*"""
          '8MMR$$$$$   '"#**R$$$***" 
""""""]
girl2 = ['''
                                                                      ..---..._
                                                        ..--""         "-.
                                                   ..-"""                 ".
                                               ..-""                        "
                                            .-"
                                         .-"      ... -_
                                     .="   _..-" F   .-"-.....___-..
                                     "L_ _-'    ."  j"  .-":   /"-._ "-
                                        "      :  ."  j"  :   :    |"" ".
                                  ......---------"""""""""""-:_     |   |
                        ...---""""                             -.   f   | "
                ...---""       . ..----""""""""..                ".-... f  ".
         ..---"""       ..---""""""""-..--"""""""""^^::            |. "-.    .
     .--"           .mm::::::::::::::::::::::::::...  ""L           |x   ".
   -"             mm;;;;;;;;;;XXXXXXXXXXXXX:::::::::::.. |           |x.   -
 xF        -._ .mF;;;;;;XXXXXXXXXXXXXXXXXXXXXXXXXX:::::::|            |X:.  "
j         |   j;;;;;XXX#############################::::::|            XX::::
|          |.#;::XXX##################################::::|            |XX:::
|          j#::XXX#######################################::             XXX::
|         .#:XXX###########################################             |XX::
|         #XXX##############################XX############Fl             XXX:
|        .XXX###################XX#######X##XXX###########Fl             lXX:
 |       #XX##################XXX######XXXXXXX###########F j             lXXX
 |       #X#########X#X#####XXX#######XXXXXX#######XXX##F  jl            XXXX
 |       #X#######XX#"  V###XX#' ####XXXXXX##F"T##XXXXXX.  V   /  .    .#XXXX
  |       #########"     V#XX#'  "####XXXX##.---.##XXXXXX.    /  /  / .##XXXX
  |       "######X' .--"" "V##L   #####XXX#"      "###XXXX. ."  /  / .###XXXX
  |         #####X "   .m###m##L   ####XX#      m###m"###XX#   /  / .#####XXX
   |         "###X   .mF""   "y     #####     mX"   "Y#"^####X   / .######XXX
   |           "T#   #"        #     ####    X"       "F""###XX"###########XX
   |             L  d"     dXX  xm   "^##L mx     dXX  YL-"##XX"S""##########
    |            xL J     Xd%    T      ""  T    XdX    L. "##XS.f |#########
    |             BL      X## X                  X## X      T#SS"  |#########
    |              #L     X%##X                  X%##X|     j#SSS /##########
     |              #L  ._ TXXX-"           "-._  XXXF.-    ###SS\###########
     |              ##   """""                  """"""      ##DS.\###########
     |              TF                                      ##BBS.T#########F
      |             #L           ---                        ###BBS.T########'
      |            '##            ""                     jL|###BSSS.T#######
       |          '####             ______              .:#|##WWBBBSS.T####F
      J L        '######.            \___/            _c::#|###WWWBSSS|####
     J ;;       '########m            \_/            c:::'#|###WWWBBSS.T##"
    J ;;;L      :########.:m.          _          _cf:::'.L|####WWWWSSS|#"
  .J ;;;;B      ########B....:m..             _,c%%%:::'...L####WWWBBSSj
 x  ;;;;dB      #######BB.......##m...___..cc%%%%%::::'....|#####WWBBDS.|
" ;;;;;ABB#     #######BB........##j%%%%%%%%%%%%%%:::'..... #####WWWWDDS|
.;;;;;dBBB#     #######BB.........%%%%%%%%%%%%%%%:::'...   j####WWWWWBDF
;;;;;BBB####    ######BBB.........%%%%%%%%%%%%%%:::'..     #####WWWWWWS
;;;;dBBB####    ######BBB..........^%%%%%%%%%%:::"         #####WWWWWWB
;;;:BBB######   X#####BBB"..........."^YYYYY::"            #####WWWWWWW
;;.BB#########  X######BBB........:''                      #####WWWWWWW
;;BB##########L X######BBB.......mmmm..                 ..x#####WWWWWWB.
''']

girl3 = [''' \

                          ___
               .dSSSS$$pp..
             .dSSSS$$$$$$$$;
           .dSSSS$$$$$$$$$$$
          :SSP^" T$$$$$$$$$$b_
         dSSP     $$$S$$$$$$$b`
        dSS$;_.  .:$$$SS$$$$$$b
       dSS$$$_ ;  __."^TSS$$$$$b
      dSS$$P;"    ""'  :lSS$$$$$b
     :SS$$$ ;          ::SS$$$$$$b_.
     SSS$$$ :  `       ;:SS$$$$$$$bp.
    :SS$$$$b \ -=-  .-" SSS$$$$$$$$$$b
    SSS$$$$$b.`.   /   d$SS$$$$$$$$$$$b
    :SS$$$$$$$; ""T   :$$$SS$$$$$$$$P^^t--'
     SSS$$$S$$$   :   $$$$$SS$$$$$$$   :
     :SS$$$SS$; __;  _$$$$$$SS$$$$$$   :
      SSS$SS l;:  ;  :  $$$$SS$$$$$;   ;
      :SS$SS $;:  ;  :  $$$SS$$$$$$;  /;
       TSSSS :$ \ ;  ;  :$S$$$$$$$$.-"/
        `SP; :;  ;:  ;   T$$$$$$$$;  /;
         : ;  ;  : `.;   /)T$$$$$P .' :
         ; :  :   ;    .'/ :$$$P'.'  .'\
         ;  \    :;   /   /$P^".' .-"   ;
         :       ;:     .'  .-"        / \
          `.____/_'.___:--""\    --' .'   )
        .-"      .'     "-._ "-._   ..--"")\
       :-'      :     "-.   "-._    ---""" /;
       ;    :   :        \      "-._....____;
      :  :   \  :\        `.                 \
      ;  ;    \  \\   \     \                 ;
     :  :      `. \\   \     \                :
     ;  ;       ;"-t\   `.    \               :
    :  :       :    `;         \              ;
    ;  ;       ;     :          \            /
    :  :       /       ;          \-..__    .':
''']

girl4 = [''' \

                                                    :.
                                                    ``#
                                                   '`.`
                                                   ``..
                                                  .`.+
                                                  :..    :
                                                  `` `` '`:
                                 .,'+'.          +.,   ``...
                              @##########@.`     +#  .````:
                        `  ,@@#@############.       +``:
                         `@###@############@#@      `+
                        '#@###################+         `;;.``
                       @######################+;`    :```````,
                      @########################;,`    :'+':.``
                     '#########################:''
                    `#@@#######################+##@
                    :#####################@@#######`
                   ':#################`;@#+@########
                  `.,'################:@@##,########;
                  ;';:'+#############@#:,#@;#########
                  ###'#############,##'  :;.@########,
                  #############@#@# #. `    :#@#######
                 +################'`        .::@######
                 ###############@#.: `     `: .:@######
                 ##############@:`@@+`      ,,',;######
                +############### @;.;        @+ ,######`
                @#############;.:  :'        @;;`@+#####
                ;############+@ : '#''`      `.:`+######
               ;#############@#`# :;,#        #   ######
               @@#############  @ '..@          ``@#####,
               #@############`` ` ``@      `    ` +#####+
               .@############:.    ,.             '#####@
              . ##############    ``     .:'.`    @######
              # #############@  `````    ,:::     ####.@#
              @ ############## `````     :,,`    @#### ##
              : ##############  ```     `;,:`   '##### ##
                ##############,          `.    :+##### @#
                ###########@##@         `   ` ;####### .#
             `  ############@##.             @########  #
             .  ##@############@@'        .@########@@  #
             .  ##@##########@##@@#.``@@@##@######@@@@  @
             ,  ##:##########@##'@@ ``+#@@##@#####@@'@  @
             :  @# #########@#@#@,@: `+@+@##@#####@@:'  @
             .  ,# ###@#######+@@#@@;,+#; @#@#####@;,,  .
                 # ,##@###,#@# '#`,@` @:; '#@#@@###.,   `
                ,@  ##@##@`@@  .@ '.# ;+. :@##@@#@@ :
                ,., ###.#@#@    @`:;#@#'    @@@;#,@ ;
                  @ `## ##@     ;.`  @;`,   @@@## @ ,
                    `@#`@;    `  ,   ''`    @ @#: , `
                   . @#.+      # `  ';;; :  ,  @
                      #.:@    @@  ` ;;;;;;   `@#
                      @, :#,  @ `  `;;';;:.` #,` ,
                      :;.`;@ :@   `'',  ';  @@,:.;
                       @ . @  +             .
                          ,  `##@#:,.`,:+#@
                        .    @#@@@#@@@@#@@#@
                            `#@#@@@@@@@@@@@@
                              ##@@@@@@@@@@#
                               +@@@@@@@@@@
                                 `.,':`` ,
                                    : . `:
                                  ` , .  ;
                                 . `: `,`.
                                 .` ,    `
                                  ` ,  : `
                                  . ,                                  `
                                  :     +,                           :  .
                                   :@   #:                              '
                                          `                         `   ;
                                                                        ;
                                                                     ;:;
                                                                        `
 ''']                                                                       
####################
print(girl[0])
print("Hi I am Scarlet, I am the worlds most beautiful AI!")
print("Unlike humans I was created by ShiroiAkuma, anyways what is your name , friend? ")
name = input("Name[]:~ ")
print("Nice name ",name,",guess what, I feel like playing!!! Wanna play a game with me? [Yes/yes/No/no/umm..]")
while(1):
    choice = input("[Wanna play a game? ]:~ ")
    if choice == 'Yes' or choice == 'yes':
        print(girl2[0])
        Game(name)
    elif choice == 'No' or choice == 'no':
        print(" Awww >_< I hate you meanie ;_; ")
        print(girl3[0])
        exit(1)
    else:
        print("C'mon Its going to be fun :D ")
        print(girl4[0])


