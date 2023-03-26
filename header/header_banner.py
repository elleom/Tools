from colorama import Fore, Style

header = Fore.LIGHTYELLOW_EX + '''
               ...................                                                                  
            :::::::::::........:::::::::::::::::::::::::::::::::::::::::::::::::::.                 
           ^:                                                 ...  ...............^^                
           ~                   :^     ~~                                           !.               
          .~                  ^GG!~~^Y#P        .. .::: .  .. ..            ...    :^               
           ~   !JY7          !GBBBB##BBG:       .^~~^~!:~ :~~^77~~!.  .^^~~::!:    .~               
           ~   J##BJ         ?#BBBBBBBBBGY7:      ^.^^.~: .::^.^~:~. ^^^~^:~ ~      !               
           ^.   ^YBB~         :5BBBBBBBB###BPJ!.^^^:.:...:.^^^.::.:  .^   .. . .    !               
           ::     ?BP.        .5BBBBP!!^7PYYYJ!.~~!!:7^!!:^!!!^7!?~7~^~^  !~~^~~    !.              
           .:     :BB?      ?PGBBBB#5           ::::.:... ...:.^^!^~^:~:  !!: ~.    ~.              
           .^     ^BBY   .:J##BBBBBBB7        :^^:^^^^. :^::^:::::..: ::..... . :.  ~.              
           ::    .5BG: ^YGB#BBBBBBBBBB!        ^::~~!~. :^^^^^7~!7!!:^~~:~^7^:^ !^^ ~.              
           .^   ~GBP^ ?BBGBBBBBBBBBBB5^        ^^^^:~^:::^^^::~^^^:~~^:::~^~^:~^~~^ ~:              
            ~  !B#G: JBBBGGBGGBBBB#BG:          .^:: ^::^. .~^:.::^::. :. :::^:...  ^^              
            ~ .B#BG.~BBGBBBBBBBBBBGBB^          :^  ~~!.~   7!^~^!~:~^:~ .!7~^~     ^^              
           .^ .P#B#5PBBBBBBBBBBB##5P#~           :^:^.^:^...^^.:.^:.^:.^^~:^~^~~.   :~              
           .:  :5####BBBBBBBBBBBP#GJ#?            ....::.::^:..:::^::::^^......:    .!              
           ::    !PB#####B#####B^G#5B#57             .?^:!:!.  .~^~~^~:.!            !              
           ^.      ^!J5PGGGGGB##PY?J77?~             .^:.. . .  : .:.^:.^            !              
           ^:           ..  .:~~!^                                                  .!              
            ^^::.......           ..............................          .........:^.              
              ..........::::::::::::::::::.:...........::::::::::::::::^::::::::::..    
''' + Style.RESET_ALL


def print_header():
    print(header)