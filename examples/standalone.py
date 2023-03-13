#!/usr/bin/env python3

# <<<<< auto-generated by daylinmorgan/viv (v.22.12a3)
# fmt: off
def _viv_activate(*pkgs: str, track_exe: bool = False, name: str = "") -> None:                               # noqa
    i,s,m,e,spec=__import__,str,map,lambda x: True if x else False,[*pkgs]                                    # noqa
    if not {*m(type,pkgs)}=={s}: raise ValueError(f"spec: {pkgs} is invalid")                                 # noqa
    ge,sys,P,ew=i("os").getenv,i("sys"),i("pathlib").Path,i("sys").stderr.write                               # noqa
    (cache:=(P(ge("XDG_CACHE_HOME",P.home()/".cache"))/"viv"/"venvs")).mkdir(parents=True,exist_ok=True)      # noqa
    ((sha256:=i("hashlib").sha256()).update((s(spec)+                                                         # noqa
     (((exe:=s(P(i("sys").executable).resolve()) if track_exe else "N/A")))).encode()))                       # noqa
    if (env:=cache/(name if name else (_id:=sha256.hexdigest()))) not in cache.glob("*/") or ge("VIV_FORCE"): # noqa
        v=e(ge("VIV_VERBOSE"));ew(f"generating new vivenv -> {env.name}\n")                                   # noqa
        i("venv").EnvBuilder(with_pip=True,clear=True).create(env)                                            # noqa
        with (env/"pip.conf").open("w") as f:f.write("[global]\ndisable-pip-version-check=true")              # noqa
        if (p:=i("subprocess").run([env/"bin"/"pip","install","--force-reinstall",*spec],text=True,           # noqa
            stdout=(-1,None)[v],stderr=(-2,None)[v])).returncode!=0:                                          # noqa
            if env.is_dir():i("shutil").rmtree(env)                                                           # noqa
            ew(f"pip had non zero exit ({p.returncode})\n{p.stdout}\n");sys.exit(p.returncode)                # noqa
        with (env/"viv-info.json").open("w") as f:                                                            # noqa
            i("json").dump({"created":s(i("datetime").datetime.today()),"id":_id,"spec":spec,"exe":exe},f)    # noqa
    sys.path = [p for p in (*sys.path,s(*(env/"lib").glob("py*/si*"))) if p!=i("site").USER_SITE]             # noqa
_viv_activate("pyfiglet==0.8.post1")                                                                          # noqa
# fmt: on
# >>>>> code golfed with <3


from pyfiglet import Figlet

if __name__ == "__main__":
    f = Figlet(font="slant")
    figtxt = f.renderText("viv").splitlines()
    figtxt[-2] += " isn't venv!"
    print("\n".join(figtxt))
