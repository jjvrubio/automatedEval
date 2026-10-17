# S39 — Browser / human inspection record

Date: 2026-09-22. Status: NOT EXECUTED / TOOL UNAVAILABLE.

The `browser:control-in-app-browser` skill was read completely. Its installed browser-client module exists, but the available tool catalogue exposes neither the required browser execution tool (`node_repl js`) nor a tool-discovery entry point that can enable it. Two catalogue searches returned no matching browser/Node execution tools; MCP resource and template inventories were empty. No in-app browser connection, page navigation, screenshot or human acceptance is claimed. No alternate automation server, dependency installation or browser installation was attempted.

This is distinct from the executed jsdom integration evidence in [the final navigation matrix](pre-delta-navigation-matrix-final.json). The latter uses actual App/provider/BrowserRouter clicks and DOM-exposed text, but is not a browser render or manual inspection. The generic document reload is explicitly modeled at the intercepted click boundary; it is not executed by jsdom.

## Unexecuted inspection protocol

These are instructions for a possible inspection, NOT results. No dev server was left running.

From the prototype directory with the existing Node >=24 toolchain, start `npm run dev -- --host 127.0.0.1`, then use the origin actually reported by Vite.

| Initial path | Initial visible identity | Selected control | Expected final path / identity |
| --- | --- | --- | --- |
| `/?demo=hospitality-family-adventure` | Aurora Stay; Lucía; jardín/fuente framing | Mi aventura | Same A URL, branding, content and progress |
| `/?demo=hospitality-family-adventure-costa` | Costa Clara Resort; Inés/Mateo; mirador/patio framing | Mi aventura | Same B URL, branding, content and progress |
| `/?demo=retail-baseline` | Convercus; Alex | Búsqueda del tesoro | `/?demo=hospitality-family-adventure`; fresh Aurora Family Adventure |
| `/?demo=hospitality-stay` | Aurora Stay; Lucía; generic Arrival Home | Búsqueda del tesoro | `/?demo=hospitality-family-adventure`; fresh Aurora Family Adventure |

For A/B, record the actual initial URL and rendered control. Click once at initial state; then advance the two available public actions to one clue, click again, navigate to Actividad and return with Mi aventura. Record final URL, brand, situated copy, clue count, any reset or crossed content. Do not infer runtime identity solely from a brand label; correlate with the integration trace or read-only runtime instrumentation in a separately authorized inspection.

Scope remains local navigation coherence. This protocol is not Safari/iOS, real-device, PWA, accessibility-complete, commercial or visual acceptance. The unavailable inspection limits those claims, but does not require a product change: the selected B→A problem assumption is already contradicted by current source reachability and executed DOM/router controls.
