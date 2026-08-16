# ORBIT Grammar v0.1 (Draft)

This is an intentionally small grammar for the first parser prototype.

```ebnf
program      = { declaration } ;
declaration  = world | location | product | evidence | flow ;
world        = "world" identifier "{" { declaration } "}" ;
location     = "location" identifier "@" number "," number ;
product      = "product" identifier "{" { property } "}" ;
evidence     = "evidence" identifier "{" { property } "}" ;
flow         = "flow" identifier "->" identifier ;
property     = identifier value ;
value        = string | number | quantity | identifier ;
quantity     = number identifier [ "/" identifier ] ;
identifier   = letter { letter | digit | "_" } ;
number       = [ "-" ] digit { digit } [ "." digit { digit } ] ;
string       = '"' { character } '"' ;
letter       = "A".."Z" | "a".."z" ;
digit        = "0".."9" ;
```

## Reserved concepts

`world`, `location`, `product`, `evidence`, and `flow` are the initial reserved words. More domain-specific constructs should be added only after a concrete use case and semantic definition exist.

## Example

```orbit
world demo {
    location Bangkok @ 13.7563, 100.5018

    product water {
        quantity 12 bottle
        price 25 THB / pack
    }

    evidence price_record {
        status sourced
        confidence 0.80
    }

    flow source -> Bangkok
}
```

## Design principle

Keep syntax small. Put complexity into typed semantics, reusable libraries and an intermediate representation rather than making the grammar enormous.
