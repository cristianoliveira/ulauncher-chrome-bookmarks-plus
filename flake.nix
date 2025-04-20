{
  description = "Nix flake";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    utils.url = "github:numtide/flake-utils";
  };
  outputs = { nixpkgs, utils, ... }: 
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python3
            python3Packages.virtualenv
            python3Packages.ruff
            # It is essential **not** to add `pip` here as
            # it would prevent proper virtualenv creation.
            inotify-tools
            ulauncher
            gtk3
            funzzy
          ];

          shellHook = ''
            # set SOURCE_DATE_EPOCH so that we can use python wheels
            SOURCE_DATE_EPOCH=$(date +%s)

            virtualenv venv

            source venv/bin/activate
          '';
        };
    });
}
