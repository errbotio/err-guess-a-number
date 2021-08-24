from errbot import FLOW_END, BotFlow, FlowRoot, botflow


class GuessFlows(BotFlow):
    """Conversation flows related to polls"""

    @botflow
    def guess(self, flow: FlowRoot):
        """This is a flow that can set a guessing game."""
        # setup Flow
        game_created = flow.connect("tryme", auto_trigger=True)
        one_guess = game_created.connect("guessing")
        one_guess.connect(one_guess)  # loop on itself
        one_guess.connect(FLOW_END, predicate=lambda ctx: ctx["tries"] == 0)
