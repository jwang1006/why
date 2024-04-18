from typing import Dict, List
import scene, cast_member

class Object:
    def __init__(self, sceneList: List[scene.Scene]) -> None:
        self.information: Dict[str, Dict[str, any]] = {scene.name: {"location": None, "movers": None} for scene in sceneList}

    def getLocationInScene(self, sceneName: str) -> str:
        return self.information[sceneName]["location"]
    
    def moveObjectInScene(self, sceneName: str, newLocation: str, movers: List[cast_member.Actor]) -> None:
        self.information[sceneName]["location"]=newLocation
        self.information[sceneName]["movers"]=movers

    def getMoversInScene(self, sceneName: str) -> str:
        return self.information[sceneName]["movers"]