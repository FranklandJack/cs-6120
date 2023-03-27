"""Utility module for shared functionality between exercises"""
from typing import OrderedDict


def build_blocks(body):
    """
    Generator that builds basic blocks from a function body.

        Parameters:
            body The function body to build the basic blocks for.

        Returns:
            Yielded basic blocks for function body
    """
    block = []

    for instr in body:
        # Check whether this is an actual instruction.
        if "op" in instr:
            # If it is we need to record it, even if it is a terminator.
            block.append(instr)

            # If we've hit a terminator that is the last instruction in the
            # block.
            if instr["op"] in ["jmp", "br", "ret"]:
                yield block
                block = []

        else:
            # In this case we've hit a label i.e. implicit fallthrough from the
            # end of BB.
            if block:
                yield block
            # We treat the label as the first "instruction" in the block so we
            # can keep track of it.
            block = [instr]

    # We've hit the end of a function i.e. implicit return so just return
    # the current block.
    if block:
        yield block


def build_block_map(blocks):
    """
    Builds a map of basic block labels to the list of instructions in the basic
    block.

    Basic blocks without labels will be given the name bX for some unique
    integer X.

        Parameters:
            blocks The list of basic blocks to build the map for.

        Returns:
            Map of basic block names to basic blocks.

    """

    # We need to use an ordered dictionary here so that callers passing an
    # ordered list of basic blocks get back a map in the same order.
    out_blocks = OrderedDict()

    for block in blocks:
        # If there is a name of the block it will be the first "op".
        if "label" in block[0]:
            # We have a name for our block.
            name = block[0]["label"]
            block = block[1:]
        else:
            # We don't have a name for our block.
            name = "b{}".format(len(out_blocks))

        out_blocks[name] = block
    return out_blocks


def build_cfg(blocks):
    """
    Builds a map of basic blocks to their successors i.e. the control flow graph.

        Parameters:
            blocks Map of basic blocks where the key is the block name and the value
            is the list of instructions in the block.

        Returns:
            A map representing the CFG.
    """
    cfg = {}
    for idx, label in enumerate(blocks):
        last_instr = blocks[label][-1]
        if last_instr["op"] in ["br", "jmp"]:
            succ = last_instr["labels"]
        elif last_instr["op"] == "ret":
            succ = []
        else:
            # It's possible there is a implict return, in whih case we are in
            # the las bb of the function and there are no successors.
            succ = [] if idx == len(blocks) - 1 else [list(blocks)[idx + 1]]

        cfg[label] = succ

    return cfg


def build_dot_cfg_for_func(func):
    """
    Builds the CFG of a functions basic blocks in the .dot format.

        Parameters:
            func The function body to build the graph for.

        Returns:
            The .dot representation of the CFG.
    """
    name2block = build_block_map(build_blocks(func["instrs"]))
    cfg = build_cfg(name2block)
    dot_cfg = "digraph {} {{\n".format(func["name"])
    for name in name2block:
        dot_cfg += "   {};\n".format(name)
    for name, succs in cfg.items():
        for succ in succs:
            dot_cfg += "   {} -> {};\n".format(name, succ)
    dot_cfg += "}"

    return dot_cfg


def build_dot_cfg_for_prog(prog):
    """
    Builds the CFG for all functions in a program.

        Parameters:
            prog The program to build the CFGs for.

        Returns:
            The .dot representation for all CFGs in the program.
    """
    dot_cfgs = ""
    for func in prog["functions"]:
        dot_cfgs += build_dot_cfg_for_func(func)
    return dot_cfgs
