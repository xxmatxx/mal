# PYTHON mal check list
- [x] Step 0: The REPL
- [ ] Step 1: Read and Print
  - [ ] reader.py
    - [ ] read_str
    - [ ] tokenize
    - [ ] read_form
    - [ ] read_list
    - [ ] read_atom
    - [ ] Handle when tokenizer retun no value
    - [ ] Tokenizer supports comments 
  - [ ] printer.py
    - [ ] pr_str
  - [ ] mal_types.py
    - [x] integer
    - [ ] float
    - [x] string
    - [x] symbol
    - [x] Nill
    - [x] Bolean
    - [x] Closure
    - [ ] Vector
    - [ ] keyword
    - [ ] hash-map
  
- [ ] Step 2: Eval
  - [ ] eval_ast
    - [ ] ast is symbol
    - [ ] ast is list
    - [ ] ast is a vector
    - [ ] ast is a hash-map
    - [ ] otherwise
  - [ ] EVAL
    - [ ] ast is not a lis
    - [ ] ast is a empty list
    - [ ] ast is a list
  
- [ ] Step 3: Environments
  - [ ] env.py
    - [ ] Env object
      - [ ] set
      - [ ] find
      - [ ] get
    - [ ] update REPL to use Enviroment
    - [ ] update step3_env.qx to use the new Env type to create the repl_env (with a nil outer value)
    - [ ] use the set method to add the numeric functions.
    - [ ] modify eval_ast to use Env get method to obtain value of symbol
  - [ ] step3 ... .py
    - [ ] EVAL function
      - [ ] def!
      - [ ] let*
      - [ ] apply
    
    
- [ ] Step 4: If Fn Do
- [ ] Step 5: Tail call optimization
- [ ] Step 6: Files, Mutation, and Evil
- [ ] Step 7: Quoting
- [ ] Step 8: Macros
- [ ] Step 9: Try
- [ ] Step A: Metadata, Self-hosting and Interop


