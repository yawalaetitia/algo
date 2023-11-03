def callback_originate(events):
    print(events)


async def Hangup_callback(events):
    if events.get("Event") == "Hangup":
        print(events)
        await ami.connection_close()


try:
    # ami = AMIClient(host="192.168.50.87", port=5038, username="tester", secret="the_tester")
    ami = AMIClient(
        host="51.91.97.8", port=5038, username="fabien", secret="fabienmanager"
    )
except Exception as e:
    print(e)

ami.create_action(
    {
        "Action": "Originate",
        "Exten": "8000",
        "Channel": "PJSIP/701",
        "Context": "from-internal",
        "Priority": "1",
        "Variable": f"NOM={fullname}",
        "Async": "true",
    },
    callback_originate,
)
ami.register_event(["Originate"], callback_originate)
ami.register_event(["Hangup"], Hangup_callback)
ami.connect()