![build](https://github.com/pingalit/pcb-ci-tester/actions/workflows/main.yml/badge.svg)

# PCB Gerber Renderer
Auto generate SVGs from Gerber Files (in .zip) for any ECAD software. Uses the gerber-renderer.py library to convert and export the gerber files to svg or pdfs.

## Example SVG output
| Top | Bottom |
:-------------------------:|:-------------------------:
| ![](documents/top.svg) | ![](documents/bottom.svg) |

## Files structure
Any .zip file in the folder gerber-files will get converted to .svg and stored in the folder "documents" or "docs".
