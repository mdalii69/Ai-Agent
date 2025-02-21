#!/usr/bin/env python

from pydantic import BaseModel
from crewai.flow import Flow, listen, start
from dotenv import load_dotenv
import assemblyai as aai
from crews.meeting_minutes_crew.meeting_minutes_crew import MeetingMinutesCrew
from crews.gmailcrew.gmailcrew import GmailCrew


load_dotenv()


class MeetingMinutesState(BaseModel):
    transcript: str = ""
    meeting_minutes: str = ""


class MeetingMinutesFlow(Flow[MeetingMinutesState]):

    @start()
    def transcribe_meeting(self):
        print("Generating Transcript...")

        # `pip3 install assemblyai` (macOS)
        # `pip install assemblyai` (Windows)

        aai.settings.api_key = "f9e3398dff8b41b7876853cca7d79c23"
        transcriber = aai.Transcriber()

        # transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
        transcript = transcriber.transcribe("c:\\Users\\alihu\\Downloads\\EarningsCall.wav")
        print(transcript.text)

    @listen(transcribe_meeting)
    def generate_meeting_minutes(self):
        print("Generating Meeting Minutes...")

        crew = MeetingMinutesCrew()
        inputs = {
            "transcript": self.state.transcript
        }
        meeting_minutes = crew.crew().kickoff(inputs=inputs)
        self.state.meeting_minutes = meeting_minutes

    @listen(generate_meeting_minutes)
    def create_draft_meeting_minutes(self):
        print("Creating Draft Meeting Minutes...")

        crew = GmailCrew()

        meeting_minutes_text = str(self.state.meeting_minutes)
    
        inputs = {
            "body": meeting_minutes_text
        }
        draft_crew = crew.crew().kickoff(inputs=inputs)
        print(f'Draft Crew: {draft_crew}')

def kickoff():
    meeting_minutes_flow = MeetingMinutesFlow()
    meeting_minutes_flow.kickoff()


if __name__ == "__main__":
    kickoff()
