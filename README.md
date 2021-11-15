# Finnish variation of programmer Dvorak 

I got interested in custom layouts and there wasn't programmer Dvorak made with finnish support so I made this.
The implementation is exactly same as Arkkudvorak so the layout utilizes the extra key under A letter to include both ä and ö using shift and Altgr a and o to get the capital variants.

# Installation

## Windows

Depending on your environment you want to either install the layout normally or use the AHK layout made for [this great program](https://github.com/DreymaR/BigBagKbdTrixPKL).

### Normal install

Head to releases tab and downlod the latest zip, then run the exe and select the layout from windows settings like any other.

### Portable/non-admin install

1. Download this repo and [this](https://github.com/DreymaR/BigBagKbdTrixPKL) repo as zip and unzip them. 
2. Copy over windows/Dvk-eD_ISO_SymFI into `<EPKL root>/layout/Dvorak` (the whole folder, not the layout.ini inside of it).
3. Run `Compile_EPKL.bat` to make executable and run it.
4. Select the layout by launching Layout/Settings from the tray icon.
5. Configure whatever else settings you want like disabling the help image (which I didn't create so it's empty) in `EPKL_Settings_Override.ini`.
