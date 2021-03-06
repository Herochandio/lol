

	"name": "python-live-coding",	"publisher": "CodeJunkie",

	"displayName": "Python Live Coding",

	"description": "Enables live execution of python code",

	"icon": "icon.png",

	"version": "1.1.6",

	"engines": {

		"vscode": "^1.36.0"

	},

	"license": "SEE LICENSE IN LICENSE.txt",

	"repository": {

		"type": "git",

		"url": "https://github.com/zys5945/PythonLiveCoding"

	},

	"categories": [

		"Other"

	],

	"activationEvents": [

		"*"

	],

	"main": "./dist/extension.js",

	"contributes": {

		"commands": [

			{

				"command": "pythonLiveCoding.execute",

				"title": "Python Live Coding: Execute"

			},

			{

				"command": "pythonLiveCoding.executeAll",

				"title": "Python Live Coding: Execute All"

			},

			{

				"command": "pythonLiveCoding.executeChunk",

				"title": "Python Live Coding: Execute Chunk"

			},

			{

				"command": "pythonLiveCoding.dispose",

				"title": "Python Live Coding: Dispose Terminal"

			}

		],

		"configuration": {

			"title": "Python Live Coding",

			"properties": {

				"pythonLiveCoding.executeUntitled": {

					"type": "boolean",

					"default": true,

					"description": "Whether to execute code in untitled documents as if they where in main script"

				},

				"pythonLiveCoding.executeNotImported": {

					"type": "boolean",

					"default": false,

					"description": "Whether to execute code in modules that are not imported as if they where in main script"

				},

				"pythonLiveCoding.interpreterPath": {

					"type": "string",

					"default": "python3",

					"description": "Path to the python interpreter to be used"

				},

				"pythonLiveCoding.reservedKeyword": {

					"type": "string",

					"default": "__python_live_coding_reserved_keyword",

					"description": "Name of the keyword that will be reserved for use in the __main__ module"

				}

			}

		},

		"keybindings": [

			{

				"command": "pythonLiveCoding.execute",

				"key": "ctrl+enter",

				"mac": "cmd+enter",

				"when": "editorTextFocus && editorLangId == python"

			},

			{

				"command": "pythonLiveCoding.executeAll",

				"key": "ctrl+shift+enter",

				"mac": "cmd+shift+enter",

				"when": "editorTextFocus && editorLangId == python"

			},

			{

				"command": "pythonLiveCoding.executeChunk",

				"key": "ctrl+alt+enter",

				"mac": "cmd+alt+enter",

				"when": "editorTextFocus && editorLangId == python"

			},

			{

				"command": "pythonLiveCoding.dispose",

				"key": "ctrl+alt+del",

				"mac": "cmd+alt+enter",

				"when": "editorTextFocus && editorLangId == python"

			}

		]

	},

	"scripts": {

		"vscode:prepublish": "webpack --mode production",

		"webpack": "webpack --mode development",

		"webpack-dev": "webpack --mode development --watch",

		"test-compile": "tsc -p ./",

		"gzip-python": "python src/gzip_load.py"

	},

	"devDependencies": {

		"@types/glob": "^7.1.1",

		"@types/mocha": "^5.2.6",

		"@types/node": "^10.12.21",

		"@types/vscode": "^1.36.0",

		"glob": "^7.1.4",

		"mocha": "^6.1.4",

		"ts-loader": "^6.0.4",

		"tslint": "^5.12.1",

		"typescript": "^3.3.1",

		"vscode-test": "^1.0.2",

		"webpack": "^4.39.3",

		"webpack-cli": "^3.3.8"

	},

	"dependencies": {

		"@types/lodash": "^4.14.137",

		"lodash": "^4.17.15"

	}

}
