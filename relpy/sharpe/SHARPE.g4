grammar SHARPE;

prog
    : ((statement)? NL)*
    ;

statement
    : bindStatement
    | markovBlock
    | bindBlock
    | ftreeBlock
    ;

bindStatement
    : ('bind'|'BIND') bindDecleration
    ;

bindDecleration returns [int type]
    : ID literal_expr {$type = 1;}
    | ID expr {$type = 2;}
    ;

bindBlock
    : ('bind'|'BIND') NL+ ((bindDecleration)? NL)* 'end'
    ;

markovBlock
    : markovBlockDecleration NL+ ((markovTransDecrelation)? NL)* (markovRewardBlock)? markovInitBlock
    ;

markovBlockDecleration
    : ('markov' | 'MARKOV') ID
    ;

markovRewardBlock
    : ('reward' | 'REWARD' ) NL+ ((markovRwdStateDecrelation)? NL)*
    ;

markovInitBlock
    : ('end' | 'END') NL+ ((markovInitStateDecrelation)? NL)* 'end'
    ;

markovTransDecrelation
    : ID ID expr
    ;

markovRwdStateDecrelation
    : ID expr
    ;

markovInitStateDecrelation
    : ID expr
    ;

ftreeBlock
    : ftreeBlockDecleration NL+ ((ftreeStatement)? NL)* 'end'
    ;

ftreeBlockDecleration
    : ('ftree' | 'FTREE') ID
    ;

ftreeStatement
    : ftreeRepeatDecrelation
    | ftreeBasicDecrelation
    | ftreeAndDecrelation
    | ftreeOrDecrelation
    | ftreeKofNDecrelation
    ;

ftreeRepeatDecrelation
    : 'repeat' ID probExpr
    ;

ftreeBasicDecrelation
    : 'basic' ID probExpr
    ;

ftreeAndDecrelation
    : 'and' ID (ID)+
    ;

ftreeOrDecrelation
    : 'or' ID (ID)+
    ;

ftreeKofNDecrelation
    : 'kofn' ID expr ',' expr ',' (ID)+
    ;

probExpr
    : expDistribution
    | probDistribution
    | cdfDistribution
    ;

expDistribution
    : 'exp' '(' expr ')'
    ;

probDistribution
    : 'prob' '(' expr ')'
    ;

cdfDistribution
    : 'cdf' '(' ID ')'
    ;

expr returns [int type]
    : op=('+'|'-') expr {$type = 1;}
    | expr op=('*'|'/') expr {$type = 2;}
    | expr op=('+'|'-') expr {$type = 3;}
    | function_expr {$type = 4;}
    | literal_expr {$type = 5;}
    | ID {$type = 6;}
    |	'(' expr ')' {$type = 7;}
    ;

function_expr
    : exp_function
    | markovprob_function
    | markovexrss_function
    | ftsysprob_function
    ;

exp_function
    : 'exp' '(' expr ')'
    ;

markovprob_function
    : 'prob' '(' ID ',' ID ')'
    ;

ftsysprob_function
    : 'sysprob' '(' ID ')'
    ;

markovexrss_function
    : 'exrss' '(' ID ')'
    ;

literal_expr
    : INT
    | FLOAT
    ;

INT: DIGIT+ ;

FLOAT
    : DIGIT+ '.' (DIGIT+)? (EXPONENT)?
    | '.' (DIGIT+)? (EXPONENT)?
    | DIGIT+ EXPONENT
    ;

ID: (DIGIT | CHAR | '.') (DIGIT+ | CHAR+ | '.' | ':' )* ;

NL : [\r\n;EOF]+ ;

WS : [ \t]+ -> skip ;

fragment
DIGIT: [0-9];

fragment
EXPONENT: [eE] ('+'|'-')? (DIGIT+)? ;

fragment
CHAR    : [a-zA-Z_] ;
