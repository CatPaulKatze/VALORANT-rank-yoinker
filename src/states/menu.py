from collections import defaultdict

class Menu:
    def __init__(self, Requests, log, presences):
        self.Requests = Requests
        self.log = log
        self.presences = presences

    def get_party_json(self, GamePlayersPuuid):
        partyOBJ = []
        for puuid in GamePlayersPuuid:
            history = self.Requests.fetch(url_type="pd", endpoint=f"/match-history/v1/history/{puuid}?startIndex=0&endIndex=2&queue=competitive", method="GET").json()
            for matches in history["History"]:
                matchID = matches["MatchID"]
                match = self.Requests.fetch(url_type="pd", endpoint=f"/match-details/v1/matches/{matchID}", method="get").json()

                partyIDs = []
                for player in match["players"]:
                    partyIDs.extend([{
                        "puuid": player["subject"],
                        "partyID": player["partyId"]
                    }])

                party_map = defaultdict(list)
                for entry in partyIDs:
                    party_map[entry["partyID"]].append(entry["puuid"])

                parties = [puuids for puuids in party_map.values() if len(puuids) > 1]
                playerParty = [puuids for puuids in parties if puuid in puuids]
                partyOBJ.extend(playerParty)

        player_connections = defaultdict(set)
        for party in partyOBJ:
            for player in party:
                player_connections[player].update(party)

        combined_parties = []
        seen_players = set()

        for player in player_connections:
            if player not in seen_players:
                connected_players = set()
                to_check = {player}

                while to_check:
                    current = to_check.pop()
                    if current not in connected_players:
                        connected_players.add(current)
                        to_check.update(player_connections[current] - connected_players)

                players_in_game = [p for p in connected_players if p in GamePlayersPuuid]
                if len(players_in_game) >= 2:
                    combined_parties.append(list(connected_players))
                seen_players.update(connected_players)

        return combined_parties

    def get_party_members(self, self_puuid, presencesDICT):
        res = []
        for presence in presencesDICT:
            if presence["puuid"] == self_puuid:
                decodedPresence = self.presences.decode_presence(presence["private"])
                if decodedPresence["isValid"]:
                    party_id = decodedPresence["partyId"]
                    res.append({"Subject": presence["puuid"], "PlayerIdentity": {"AccountLevel":
                                                                                     decodedPresence["accountLevel"]}})
        for presence in presencesDICT:
            decodedPresence = self.presences.decode_presence(presence["private"])
            if decodedPresence["isValid"]:
                if decodedPresence["partyId"] == party_id and presence["puuid"] != self_puuid:
                    res.append({"Subject": presence["puuid"], "PlayerIdentity": {"AccountLevel":
                                                                                     decodedPresence["accountLevel"]}})
        self.log(f"retrieved party members: {res}")
        return res