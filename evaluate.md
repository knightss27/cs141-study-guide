# Evaluate.py Solutions

1. Basic Recursion

    a. Evaluate `f1a(5, 3)` = `243`

    ```
    f1a(5, 3)                   > 243
    - f1a(4, 3)                 > 81
        - f1a(3, 3)             > 27
            - f1a(2, 3)         > 9
                - f1a(1, 3)     > 3
                    - f1a(0, 3) > 1
    ```

    b. Evaluate `f1b(6, 3)` = `243`

    ```
    f1b(6, 3)                   > 243
    - f1b(5, 3)                 > 81
        - f1b(4, 3)             > 27
            - f1b(3, 3)         > 9
                - f1b(2, 3)     > 3
                    - f1b(1, 3) > 1
    ```

    c. Evaluate `f1c(7, 3)` = `9`

    ```
    f1c(7, 3)                   > 9
    - f1c(5, 3)                 > 3
        - f1c(3, 3)             > 1
            - f1c(2, 3)         > 1
                - f1c(1, 3)     > 1
    ```

2. Basic Loops

    a. Evaluate `f2a(7, 3)` = `6`

    ```
    c = 0
        + 0
        + 1
        + 2
        + 3
    
    c = 6
    ```

    b. Evaluate `f2b(3, 10)` = `"ZPZPZP"`

    ```
    s = ""
      = "3"
      = "33"
      = "333"
      = "3333"
      = "33333"
      = "333333"
      = "ZPZPZP"
    ```

    c. Evaluate `f2c(3, 5)` = `[3   , 2   , 2   , None, None]`

    ```
    l = [None, None, None, None, None]
      = [3   , 2   , None, None, None]
      = [3   , 3   , 2   , None, None]
      = [3   , 2   , 2   , None, None]
      = [3   , 3   , 2   , None, None]
      = [3   , 2   , 2   , None, None]
      = [3   , 2   , 2   , None, None]
    ```

3. Recursion with Loops

    a. Evaluate `f3a(5, 3)` = `[0, 0, 0, 0]`

    ```
    f3a(5, 3)                   > [0, 0, 0, 0]
    - f3a(4, 3)                 > [0, 0, 0, 0]
        - f3a(3, 3)             > [0, 0, 0, 0]
            - f3a(2, 2)         > [0, 0, 0]
                - f3a(1, 1)     > [0, 0]
                    - f3a(0, 0) > [0]
    ```
    
    b. Evaluate `f3b(3, 2)` = `['3p', '3r', '3a', '2p', '2r', '1p']`

    ```
    f3b(3, 2)           > ['3p', '3r', '3a', '2p', '2r', '1p']
    - f3b(2, 2)         > ['2p', '2r', '1p']
        - f3b(1, 2)     > ['1p']
            - f3b(0, 2) > []
    ```

    c. Evaluate `f3c(5, 2)` = `"hi,hey,bye.hi,hey,bye."`
    
    ```
    f3c(5, 2)       > "hi,hey,bye.hi,hey,bye."
    - f3c(4, 1)     > "hey,bye."
        - f3c(4, 0) > "bye."
    ```