import argparse
import json
from pathlib import Path

from .mapper import build_packet, load_json
from .verify import check_packet


def cmd_build(args):
    receipt = load_json(args.receipt)
    packet = build_packet(receipt)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    print(f"packet written: {out}")


def cmd_verify(args):
    packet = load_json(args.packet)
    ok = check_packet(packet)
    print("verification passed" if ok else "verification failed")
    raise SystemExit(0 if ok else 1)


def main():
    parser = argparse.ArgumentParser(prog="elyria-wrap")
    sub = parser.add_subparsers(dest="cmd", required=True)

    build = sub.add_parser("build", help="Build a compliance evidence packet from a boundary receipt")
    build.add_argument("receipt")
    build.add_argument("--out", required=True)
    build.set_defaults(func=cmd_build)

    verify = sub.add_parser("verify", help="Verify a compliance evidence packet hash")
    verify.add_argument("packet")
    verify.set_defaults(func=cmd_verify)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
