# Moved [here](https://github.com/Sorrowfall/Resource-Packager)

# Minecraft Resource Pack Builder

Generate Minecraft resource packs from multiple directories, to create multiple resource packs with shared resources but different artstyles.

## Usage

**[Click Here](https://github.com/Soumeh/resource-pack-example/generate)** to create a new repository with the workflow already set up.
Rememember to edit `.github/workflows/compile-pack.yml`

### Example Workflow

```yaml
name: build-resource-pack
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v2
      # copy-paste this part for however many packs you want to build
      - name: Build resource pack
        uses: Soumeh/build-resource-pack@master
        with:
          # The name of the built pack
          filename: MyPack
          # The directories / files to be built into the pack
          # Directories take priority as they go down the list, replacing any files from the above directories
          items: |
            folder1
            folder2
          # Whether or not to generate a Sha1 hash of the built pack 
          # Useful for server resource packs
          # default: false
          gen-sha1: false
          # The directory to output files in
          output-folder: build
      - name: Publish
        uses: github-actions-x/commit@v2.8
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          push-branch: 'build'
          commit-message: 'compile packs'
          name: Compiler[bot]
          email: my.github@email.com 
```

### Inputs

| Name | Description | Default |
| - | - | - |
| `filename` | The name of the built pack | none |
| `items` | The folders / files to be built into the pack | none |
| `configuration-path` | Whether or not to generate a Sha1 hash of the built pack | `false` |
| `output-folder` | The directory to output files in | `build` |
