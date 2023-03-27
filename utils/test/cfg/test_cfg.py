import cfg
import json
import sys

if __name__ == '__main__':
    print(cfg.build_dot_cfg_for_prog(json.load(sys.stdin)))
