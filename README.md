# openui5-i18n-util

We all know, developers are pretty lazy, it's a solid reality.

This script will search all your i18n strings and build auto-magically (while you're drinking your deserved cup  of coffe) every translations file for you.

## Installation

Download the project wherever you want, no dependency needed (apart from python 2.7)

## Command line parameters

| Short Version | Long Version | Required | Default | Description
| :---- | :------------------- | :---- | :---------  | :---------
| -pf | --project_folder | Yes | None | Project's root folder
| -if | --i18n_folder    | Yes | None | i18n root folder
| -fp | --file-patterns  | No  | ['*.xml', '*.js'] | Array of file extension pattern patterns where to search i18n strings
| -ip | --i18n-patterns  | No | ['{i18n>([^}]+)}'] | Array of i18n patterns
| -l  | --languages      | No | ['en'] | Array of languages supported by your project
| -ml | --main-language  | No | 'en'   | Project's main language 
|

## Usage

#### Command Line Example

    python build_i18n.py --project-folder C:\Users\Emanuele\workspace\my-awesome-project --i18n-folder C:\Users\Emanuele\workspace\my-awesome-project\i18n --languages en it --main-language en


## History

#### 06/03/2017 

First commit yay!

## Credits

Emanuele Ricci

 - Email: [stermi@gmail.com](stermi@gmail.com)
 - Twitter: [@StErMi](https://twitter.com/StErMi)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
