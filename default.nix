{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication {
  propagatedBuildInputs = [
    pkgs.ffmpeg
  ];
  pname = "yibasuo";
  src = ./.;
  version = "0.1";
}

