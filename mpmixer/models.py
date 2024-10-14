from pydub import AudioSegment


class Part:
    def __init__(self, id: int, name: str, file_name: str):
        self.id = id
        self.name = name
        self.file_name = file_name
        self.audio = None


class Music:
    def __init__(self):
        self.parts: list[Part] = list()
        self.last_id = 0

    def __iter__(self):
        return iter(self.parts)

    def __getitem__(self, id):
        return [part for part in self.parts if part.id == id][0]

    def create_part(self, name: str = None, file_name: str = None):
        id = self.last_id + 1
        self.last_id = id
        part = Part(id, name, file_name)
        self.parts.append(part)
        return part

    def read_parts(self):
        return self.parts

    def update_part(self, part: Part):
        id = part.id
        index = [i for i, p in enumerate(self.parts) if p.id == id][0]
        self.parts[index] = part

    def delete_part(self, id: int):
        # idが一致する要素のインデックスを取得
        index = [i for i, part in enumerate(self.parts) if part.id == id]
        # 要素を削除
        for i in index:
            self.parts.pop(i)

    def mix(self):
        audio_long = 0
        for part in self.parts:
            part.audio = AudioSegment.from_file(part.file_name)
            audio_long = max(audio_long, len(part.audio))
        output = AudioSegment.silent(duration=audio_long)
        for part in self.parts:
            output = output.overlay(part.audio)
        return output
