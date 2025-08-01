<h1 align="center"> VALORANT rank yoinker</h1>

[![Downloads][downloads-shield]][downloads-url] 
 
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
  </ol>

    
## About The Project

 ![Screenshot](assets/Example.png)
 ![Skin Showcase Image](assets/SkinShowcase.png)

|Current Skin|Current Rank|Rank Rating|Peak Rank|Account Level|
|:---:|:---:|:---:|:---:|:---:|
|![Skin](assets/Skin.png)|![Rank](assets/Rank.png)|![Rating](assets/Rating.png)|![Peak](assets/PeakRank.png)|![Level](assets/Level.png)|
    

## Usage
 **VALORANT must be open**.

### Bundled Release:

1) Download [Microsoft Visual C++ Libraries](https://github.com/abbodi1406/vcredist/releases)
2) Download the [release](https://github.com/CatPaulKatze/VALORANT-rank-yoinker/releases/latest).
3) Extract **all** files.
4) Run vRY.exe.

### Running from source:

1) Download Python [3.11](https://www.python.org/downloads/release/python-3119/) or [3.10](https://www.python.org/downloads/release/python-31011/), make sure it is added to the PATH. (This is an option on installation.)
2) Download the [source](https://github.com/isaacKenyon/VALORANT-rank-yoinker/archive/refs/heads/main.zip).
3) Run **`INSTALL.bat`** file (or use `pip install -r requirements.txt` in the terminal)
4) Run **`START.bat`** file (or use `python main.py` in the terminal)

### Compiling from source:

1) `pip install cx_Freeze`
2) `python setup.py build`
3)  Open the new Build folder and find vRY.exe.

> `-` You can change the desired weapon by editing the gun in `config.json`, or by deleting the file for vRY re-prompt you.

> `-` View all skins: <https://vry.netlify.app/matchLoadouts>.

### Letting Github Build It:

The latest commits to the `main` branch will be built by a [Github Actions](https://github.com/CatPaulKatze/VALORANT-rank-yoinker/actions) workflow 
and a successful build should result in a compiled artifact that you can download and try out.
See the [Actions tab](https://github.com/CatPaulKatze/VALORANT-rank-yoinker/actions), click on the `Build` workflow, 
select a particular workflow run, and it should have an artifact available for download. 

If you want to make a small change to the application, you can:
1) [Fork](https://github.com/CatPaulKatze/VALORANT-rank-yoinker/fork) this project.
2) Change the code in your forked repository.
3) Let the Github Actions workflow build vRY.exe for you.
4) Download it and test it.
5) Submit a Pull Request if you would like your change included in future releases.

## Contributing

 Any contributions you make are **greatly appreciated**.

## Acknowledgements

 - [Valorant-API.com](https://valorant-api.com/)
 
## Disclaimer

 THIS PROJECT IS NOT ASSOCIATED OR ENDORSED BY RIOT GAMES. Riot Games, and all associated properties are trademarks or registered trademarks of Riot Games, Inc.
    
 Use this project at your own risk. The author is not responsible for any bans or other consequences that may arise from using this tool.


[downloads-shield]: https://img.shields.io/github/downloads/CatPaulKatze/VALORANT-rank-yoinker/total?style=for-the-badge&logo=github
[downloads-url]: https://github.com/CatPaulKatze/VALORANT-rank-yoinker/releases/latest
