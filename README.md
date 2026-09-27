# Dragons Bunker manual admins

No Discord bot, linking channel, VRChat credentials or repository secrets needed.

## Initial setup
1. Put these files at the root of aerowolf1/dragons-bunker-access on branch main, including .github/workflows/publish.yml.
2. In repository Settings > Pages, set Source to GitHub Actions.
3. Run Publish manual admin roster from Actions if the initial deployment did not run automatically.
4. Check https://aerowolf1.github.io/dragons-bunker-access/data.json returns JSON. This URL is not live until deployment succeeds.
5. Set that URL on the Unity Reader, save, and upload the world once.

## Add or remove an admin
Edit admins.txt on GitHub. Put each person's exact VRChat DISPLAY NAME on a separate line; remove their line to revoke remote admin access. Commit the change. Actions publishes it automatically. Keep spelling, capitalization, spaces and Unicode characters exact. Update the list if a person changes their display name.

The list begins empty. The four hidden built-in admins and instance owner/master still have independent access. Removing their names from this file will not revoke that independent access.

Remote admins may operate both access guns and DJ controls. The guns continue to grant/revoke temporary DJ access only. No Discord role, folder per person, user-ID conversion or bot linking is involved.

The world checks at startup and every five minutes. Allow additional time for Pages deployment/caching. A successfully downloaded manual roster does not expire solely because it has not been edited. If hosting is unavailable, a running client retains its last downloaded list for the session; a new client gets no remote privileges until a download succeeds. Built-in/host access remains. This is convenience access control, not a security boundary against modified clients.

Only _site/ is published; it contains the names and generated timestamp. The roster is public even if the source repository is private. No secrets should be stored in these files.
