# .rel File Debugger
Tool for parsing the .rel file format and displaying the data in a human readable format.

Usage: `py rel_reader.py <rel file> [--options]`

Extra options:
* `--hideops`: will hide the assumed opcode mnemonics in the code output section, instead displaying the raw hex value
* `--ws`: shows whitespace lines where there is no code in the code output section. Inserts an empty line instead of skipping lines.
* `--header`: will display only the header information for the `.rel` file
* `--legacy_off`: will disable concatenation of `0D 0A` pairs. Old REL format requires that `0D 0A` be read as `0A` when parsing.

## Requirements: 
* Python 3.6 or higher

If you are having issues with `py` opening up the Windows Store, make sure to turn off the python app execution alias in `Settings > Apps > Apps & Features > App Execution Aliases`.






---

```
rel_reader is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
