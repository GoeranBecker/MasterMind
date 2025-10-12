{ pkgs ? import <nixpkgs> {} }:

let
  devDependencies = {
    python = pkgs.python3;
    nodejs = pkgs.nodejs;
  };
in
pkgs.mkShell {
  name = "Mastermind";

  buildInputs = builtins.attrValues devDependencies;

  shellHook = ''
    echo "Dev-Environment for Mastermind"

    ${builtins.concatStringsSep "\n" (
      map (name: ''
        echo "${name}: ${devDependencies.${name}.version}"
      '') (builtins.attrNames devDependencies)
    )}

    source env/bin/activate
  '';
}
