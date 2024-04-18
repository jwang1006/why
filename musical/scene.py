from types import List
import cast_member, object
class Scene:
    def __init__(self, sceneName, actors: List[cast_member.Actor]=[], propsNeeded: List[object.Object]=[]) -> None:
        self.sceneName = sceneName
        self.actors = actors
        self.propsNeeded = propsNeeded

