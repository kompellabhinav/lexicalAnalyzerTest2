# Lexical Analyzer

### Rules
- Code begins with `play` and ends with `stop`. Each lexeme is seperated by a space.

### Statements 
- Assignment
- Delaration
- Condition
- Loops

## Token List
---

## Mathematical Operations
| Token Code       | Operation | Regex |                                
| ---------------- | --------- | ----- |
| PLUS             | +         | +     |
| MINUS            | -         | -     |
| MULTIPLY         | \*        | \*    |
| DIVIDE           | /         | /     |
| MODULUS          | %         | %     |
| OPEN             | (         | )     |
| CLOSE            | )         | )     |


## Comparisions
| Token Code | Operation | Regex |
| ---------- | --------- | ----- |
| Lesser     | <         | <     |
| Greater    | >         | >     |
| LessEqual  | <=        | <=    |
| GreatEqual | >=        | >=    |
| Equal      | ==        | ==    |
| NotEqual   | !=        | !=    |

## Integer Types
| Token Code | Size    |
| ---------- | ------- |
| Small      | 1 byte  |
| Medium     | 2 bytes |
| Large      | 4 bytes |
| Huge       | 8 bytes |


## Keywords
| Token Code | Regex          |
| ---------- | -------------  |
| VARIABLE   | [_a-zA-Z]{6,8} |
| CONDITION  | condition      |
| LOOP       | loop           |
| PLAY       | play           |
| STOP       | stop           |

## Other
| Token Code       | Operation | Regex |
| ---------------- | --------- | ----- |
| ASSIGNMENT       | =         | =     |
| BLOCKBEGIN       | {         | {     |
| BLOCKFINISH      | }         | }     |

## Priority Order
- ()
- /
- \+
- \-
- \*
- %

## Production Rules

```txt
<Program> --> play <stmt_list> stop
<stmt_list> --> {<stmt> `;`}
<stmt> --> <if_stmt> | <while_stmt> | <as_s>  | <declaration>
<if_stmt> --> condition <bool> `{` { <stmt> ';'} `}`
<while_stmt> --> loop `{` <bool> { <stmt> ';' } `}`
<as_s> --> <var> `=` <expression> `;`
<declaration> --> <datatype> <var> `;`

<datatype> --> (XS|S|L|XL)
<var> -->  [a-zA-Z_]{6,8}               
<expression> --> <term> { (`*`|`\` ) <term> }
<term> --> <term> { (`+`|`-`) <term> }
<factor> --> [0-9]+ | <var>  | `(` <expression> `)`
<bool> --> <expression> (`<=`|`>=` | `<` | `>`) <expression>


E -> E + T          Expression + Term
E -> E - T          Expression - Term
E -> T              Some expression can be a term
T -> T * F          Term * Factor
T -> T / F          Term / Factor
T -> F              Some Terms can be Factors
F -> -F             Unary Minus
F -> +F             Unary Plus
F ->( E )           Factor can be an Expression in parentheses
F -> c              Factor can be a constant
```

### To run
Give the file name in the index.py to run the code.


## (C) Is it LL Grammar ?
The code works on the principle of LR grammar and wouldn't have pairwise disjointness. It fillows push down or top down automata

## (D) Is the Grammar Ambiguous ?
The LR table would have highlighted the ambiguous parts in red which is in the action block. The following image shows that there isn't any ambiguity.