BLOCKS = [
    """[][]
[][]""",
    """[][][][]""",
    """[]    
[][][]""",
    """    []
[][][]""",
    """  []  
[][][]""",
    """[][]  
  [][]""",
    """  [][]
[][]  """,
]


def rotate_block(block: str) -> str:
    """
    [][]          []
      [][]  =>  [][]
                []
    """

    vector_block = list()
    for layer in block.split("\n"):
        vector_layer = list()
        block = ""

        for val in layer:
            block += val
            if block in ["[]", "  "]:
                vector_layer.append(block)
                block = ""

        vector_block.append(vector_layer)

    rotated_block = list()
    for j in range(len(vector_block[0])):
        rotated_layer = list()
        for i in range(len(vector_block)):
            rotated_layer.append(vector_block[len(vector_block) - 1 - i][j])
        rotated_block.append("".join(rotated_layer))

    return "\n".join(rotated_block)
