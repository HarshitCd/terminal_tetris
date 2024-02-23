from terminal_tetris import blocks


def main() -> None:
    for block in blocks.BLOCKS:
        print(
            f"{block}\n  =  \n{blocks.rotate_block(block)}\n  =\
            \n{blocks.rotate_block(blocks.rotate_block(block))}\n  =\
            \n{blocks.rotate_block(blocks.rotate_block(blocks.rotate_block(block)))}"
        )
        print("--------------------")


if __name__ == "__main__":
    main()
