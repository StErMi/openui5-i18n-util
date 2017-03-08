# openui5-i18n-util

We all know, developers are pretty lazy, it's a solid reality.

This script will search all your i18n strings and build auto-magically (while you're drinking your deserved cup  of coffe) every translations file for you.

### Restrictions

 - It's not supporting smart-merge. This script will override manual translations added in your i18n folder but it will keep older one that matches pattern
 - It does not support (at the moment) parametric i18n (but I'm working on it)

## Installation

Download the project wherever you want, no dependency needed (apart from python 2.7)

## Command line parameters

| Short Version | Long Version | Required | Default | Description
| :---| :----------------- | :---| :----------------- | :---------
| -pf | --project-folder   | Yes | None               | Project's root folder
| -if | --i18n-folder      | Yes | None | i18n root folder
| -fp | --file-patterns    | No  | ['*.xml', '*.js']  | Array of file extension pattern patterns where to search i18n strings
| -ip | --i18n-patterns    | No  | ['{i18n>([^}]+)}'] | Array of i18n patterns
| -l  | --languages        | No  | ['en']             | Array of languages supported by your project
| -ml | --main-language    | No  | 'en'               | Project's main language 

## Usage

#### Command Line Example

    python build_i18n.py --project-folder C:\Users\Emanuele\workspace\my-awesome-project --i18n-folder C:\Users\Emanuele\workspace\my-awesome-project\i18n --languages en it --main-language en


## History

#### 07/03/2017 

 - Added comment inside translation to trace from which file the i18n comes from

#### 06/03/2017 

- First commit yay!

## Credits

Emanuele Ricci

 - Email: [stermi@gmail.com](stermi@gmail.com)
 - Twitter: [@StErMi](https://twitter.com/StErMi)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
