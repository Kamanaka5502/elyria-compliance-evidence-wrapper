import argparse
import json
from pathlib import Path

from .mapper import build_packet, load_controls, load_json, verify_packet


def cmd_build(args):
    receipt = load_json(args.receipt)
    controls = load_controls(args.controls)
    packet = build_packet(receipt, controls)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    print(f"wrote {out}")
    print(packet["packet_hash"])


def cmd_verify(args):
    packet = load_json(args.packet)
    ok = verify_packet(packet)
    print(json.dumps({"ok": ok, "packet_hash": packet.get("packet_hash")}, indent=2))
    raise SystemExit(0 if ok else 1)


def main():
    parser = argparse.ArgumentParser(prog="elyria-compliance-wrapper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    build = sub.add_parser("build", help="Build a compliance evidence packet from a boundary receipt")
    build.add_argument("--receipt", required=True)
    build.add_argument("--controls", default="configs/control_map.yaml")
    build.add_argument("--out", required=True)
    build.set_defaults(func=cmd_build)

    verify = sub.add_parser("verify", help="Verify a compliance evidence packet hash")
    verify.add_argument("--packet", required=True)
    verify.set_defaults(func=cmd_verify)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
