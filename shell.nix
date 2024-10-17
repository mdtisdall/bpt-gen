let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    pkgs.gnuradio
    (pkgs.python3.withPackages (python-pkgs: [
    ]))
  ];
}
