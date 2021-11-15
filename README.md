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

## Linux

Linux directory has two files, one to define the actual layout and one to register it as usable layout to the system.

### Installing
1. Download/Clone this repository and unzip it if needed.
2. Copy `dvpfi` to `/usr/share/X11/xkb/symbols` and `evdev.xml` to `/usr/share/X11/xkb/rules`.
3. Go to your desktop environment's layout settings and select the layout.

NOTE: This install method replaces your layout definitions with mine (from recent Arch install) so if you have custom layouts or your file is different otherwise you might want to add the layout to your file yourself by adding following to your own evdev.xml:
```
<layoutList>
    ...
    <layout>
      <configItem>
        <name>dvpfi</name>
        <shortDescription>fi</shortDescription>
        <description>Finnish programmer dvorak</description>
        <languageList>
          <iso639Id>fi</iso639Id>
        </languageList>
      </configItem>  
    </layout>
    ...
</layoutList>
```

I also haven't figured out how to prevent updates from overwriting the changes.

## MacOS

There is no MacOS version, if you feel like donating me an M1 mac for creating this layout you are welcome to do so.

# Credits

- [ArkkuDvorak](http://arkku.com/dvorak/) for the idea of making use of the extra key
- [EPKL](https://github.com/DreymaR/BigBagKbdTrixPKL) for great tool and already having programmer Dvorak available
- [TAKBL](https://github.com/tonyaldon/keyboard-layout) for having nice readme that explains what is needed for adding layout to Linux
- People who designed the Dvorak, Programmer Dvorak and ArkkuDvorak
