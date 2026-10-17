# S36 current source excerpts — direct inspection; no execution

## src/demo-factory/contracts.ts
SHA256 60a58bdbee08ed21760bda8805b4b23376440623f949561ed958ac8464983c64
```text
6: export interface MemberReadModel {
7:   id: string;
8:   name: string;
9:   fullName: string;
10:   initials: string;
11:   level: string;
12:   nextLevel: string;
13:   points: number;
14:   progress: number;
15:   pointsToNextLevel: number;
16:   memberSince: string;
17: }
```
```text
36: export interface ActivityItem {
37:   id: string;
38:   title: string;
39:   description: string;
40:   occurredAt: string;
41:   displayDate: string;
42:   points?: number;
43:   tone: "cyan" | "pink" | "blue";
44:   icon: IconName;
45:   provenance: "mocked" | "simulated";
46: }
47: 
48: export interface AppSnapshot {
49:   member: MemberReadModel;
50:   coupons: CouponReadModel[];
51:   news: NewsReadModel[];
52:   activity: ActivityItem[];
53:   scenario?: {
54:     checkpoint: string;
55:     availableActionId?: string;
56:   };
57:   guestPerspective?: GuestPerspectiveReadModel;
58:   supervisionPerspective?: SupervisionPerspectiveReadModel;
59: }
60: 
61: // Local experimental demo state, not a productive enlistment contract.
62: export type DemoSubjectState = "not-enlisted" | "not-enabled" | "enabled";
63: 
64: export interface GuestPerspectiveReadModel {
65:   huntName: string;
66:   state: "ready" | "active" | "exploring" | "complete";
67:   message: string;
68:   discoveredClueCount: number;
69:   sessionLabel: string;
70:   subjects: Array<{ id: string; label: string; status: string; clueCount: number }>;
71: }
72: 
73: export interface SupervisionPerspectiveReadModel {
74:   subjects: Array<{
75:     id: string;
76:     exists: true;
77:     operationalState: DemoSubjectState;
78:     evidenceCount: number;
79:   }>;
80:   sessionSubjectRef?: string;
81:   evidence: Array<{
82:     id: string;
83:     subjectRefs: string[];
84:     type: string;
85:     provenance: string;
86:   }>;
87:   jointAdmissibility: "established" | "cannot-currently-establish";
88:   sufficiency: "established" | "not-established" | "not-attempted";
89:   derivedClaim: "established" | "not-established" | "not-produced";
90: }
```
```text
100: export interface ActivitySourceRecord {
101:   id: string;
102:   kind: ActivityKind;
103:   title: string;
104:   description: string;
105:   occurredAt: string;
106:   points?: number;
107:   provenance: "mocked" | "simulated";
108: }
109: 
110: export interface DemoFixture {
111:   id: string;
112:   member: MemberReadModel;
113:   coupons: CouponReadModel[];
114:   news: NewsReadModel[];
115:   activityRecords: ActivitySourceRecord[];
116: }
117: 
118: export interface SubjectReference {
119:   type: "individual" | "group";
120:   id: string;
121:   role: string;
122: }
123: 
124: export interface ContextReference {
125:   type: "booking" | "stay" | "property";
126:   id: string;
127: }
```
```text
185: export interface ExperienceDefinition {
186:   id: string;
187:   name: string;
188:   tesBaseline: string;
189: }
190: 
191: export interface ScenarioDefinition {
192:   id: string;
193:   experienceRef: string;
194:   subjects: SubjectReference[];
195:   contexts: ContextReference[];
196:   checkpoints: string[];
197:   // Checkpoints describe controlled demo runtime state, not TES Progression.
198:   initialCheckpoint: string;
199:   operationalSessionSubjectRef?: string;
200:   initialSubjectStates?: Record<string, DemoSubjectState>;
201:   presenterAction: {
202:     actionId: string;
203:     fromCheckpoint: string;
204:     toCheckpoint: string;
205:   };
206:   actions?: Array<{
207:     actionId: string;
208:     fromCheckpoint: string;
209:     toCheckpoint: string;
210:     kind?: "enlist" | "activate" | "evidence";
211:     subjectRef?: string;
212:     requiresEnabledSubject?: boolean;
213:     evidenceType?: string;
214:   }>;
215: }
216: 
217: export interface DemoScript {
218:   id: string;
219:   scenarioRef: string;
220:   initialCheckpoint: string;
221:   // H27: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
222:   // Display relation only; no account, authentication or subject identity claim.
223:   subjectPresentations?: Array<{ subjectRef: string; label: string }>;
224:   // H30: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
225:   // Existing available affordance -> situated message, never runtime authority.
226:   // Available action is not journey state; no viewer or TES Progression relation.
227:   experimentalJourneyPresentations?: Array<{ availableActionId: string; message: string }>;
228:   // H32: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
229:   // Static introduction for the selected demonstration, not runtime truth,
230:   // branding, journey state or a viewer/subject/stay relationship.
231:   experimentalIntroductoryFraming?: string;
232:   steps: Array<{
233:     id: string;
234:     presenterLabel: string;
235:     // H25: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
236:     // Presentation after an accepted Evidence action, never factual authority.
237:     // Independent of presenterLabel (the before-action affordance).
238:     activityPresentation?: {
239:       title: string;
240:       description: string;
241:     };
242:     expectedCheckpoint: string;
243:     action: DemoAction | DemoEnableAction;
244:   }>;
245: }
246: 
247: export interface BrandArtifact {
248:   id: string;
249:   name: string;
250:   logoUrl: string;
251:   cssVariables: Record<string, string>;
252: }
253: 
254: export interface ResolvedCapability extends CapabilityRequest {
255:   providerId: string;
256:   status: CapabilityStatus;
257:   provenance: string;
258: }
259: 
260: export interface ResolvedDemoRuntime {
261:   manifest: DemoManifest;
262:   brand: BrandArtifact;
263:   experience?: ExperienceDefinition;
264:   scenario?: ScenarioDefinition;
265:   script?: DemoScript;
266:   provider: DemoProvider;
267:   capabilities: ResolvedCapability[];
```

## src/demo-factory/artifacts.ts
SHA256 96e14628e93f2da9bd50da7c5f71c5f4d5db048960eb20659d4452a035518d53
```text
19:   "brand:aurora-stay@1": {
20:     id: "aurora-stay",
21:     name: "Aurora Stay",
22:     logoUrl: auroraStayLogoUrl,
```
```text
44: export const experiences: Record<string, ExperienceDefinition> = {
45:   "experience:arrival-welcome@1": {
46:     id: "arrival-welcome",
47:     name: "Llegada acompañada",
48:     tesBaseline: "TES_CONVERCUS_BUILDER_2026_07_R1",
49:   },
50:   "experience:family-adventure@1": {
51:     id: "family-adventure",
52:     name: "Aventura Familiar",
53:     tesBaseline: "TES_CONVERCUS_BUILDER_2026_07_R1",
54:   },
55: };
```
```text
79:   "scenario:family-adventure@1": {
80:     id: "family-adventure",
81:     experienceRef: "experience:family-adventure@1",
82:     subjects: [
83:       { type: "individual", id: "subject-p1", role: "guest" },
84:       { type: "individual", id: "subject-p2", role: "guest" },
85:     ],
86:     contexts: [
87:       { type: "property", id: "aurora-resort" },
88:       { type: "booking", id: "AS-8842" },
89:       { type: "stay", id: "stay-AS-8842" },
90:     ],
91:     checkpoints: ["ready", "clue-a-discovered", "adventure-established"],
92:     initialCheckpoint: "ready",
93:     operationalSessionSubjectRef: "subject-p1",
94:     initialSubjectStates: { "subject-p1": "not-enlisted", "subject-p2": "not-enabled" },
95:     presenterAction: {
96:       actionId: "enlist-p1",
97:       fromCheckpoint: "ready",
98:       toCheckpoint: "ready",
99:     },
100:     actions: [
101:       {
102:         actionId: "enlist-p1",
103:         fromCheckpoint: "ready",
104:         toCheckpoint: "ready",
105:         kind: "enlist",
106:         subjectRef: "subject-p1",
107:       },
108:       {
109:         actionId: "discover-clue-a",
110:         fromCheckpoint: "ready",
111:         toCheckpoint: "clue-a-discovered",
112:         kind: "evidence",
113:         subjectRef: "subject-p1",
114:         requiresEnabledSubject: true,
115:         evidenceType: "treasure_hunt.marker-a",
116:       },
117:       {
118:         actionId: "activate-p2",
119:         fromCheckpoint: "clue-a-discovered",
120:         toCheckpoint: "clue-a-discovered",
121:         kind: "activate",
122:         subjectRef: "subject-p2",
123:       },
124:       {
125:         actionId: "discover-clue-b",
126:         fromCheckpoint: "clue-a-discovered",
127:         toCheckpoint: "adventure-established",
128:         kind: "evidence",
129:         subjectRef: "subject-p2",
130:         requiresEnabledSubject: true,
131:         evidenceType: "treasure_hunt.marker-b",
132:       },
133:     ],
134:   },
135: };
136: 
```
```text
175:   "script:family-adventure@1": {
176:     id: "family-adventure",
177:     scenarioRef: "scenario:family-adventure@1",
178:     initialCheckpoint: "ready",
179:     experimentalIntroductoryFraming: "Una aventura de pistas entre el jardín y la fuente.",
180:     subjectPresentations: [
181:       { subjectRef: "subject-p1", label: "Lucía" },
182:       { subjectRef: "subject-p2", label: "Huésped 2" },
183:     ],
184:     experimentalJourneyPresentations: [
185:       { availableActionId: "discover-clue-a", message: "Exploración disponible en el jardín." },
186:       { availableActionId: "activate-p2", message: "Pista del jardín registrada. La siguiente acción está disponible." },
187:       { availableActionId: "discover-clue-b", message: "Nueva exploración disponible en la fuente." },
188:     ],
189:     steps: [
190:       {
191:         id: "enlist-p1",
192:         presenterLabel: "Alistarme",
193:         expectedCheckpoint: "ready",
194:         action: {
195:           type: "scenario_action",
196:           actionId: "enlist-p1",
197:           operation: "enlist",
198:         },
199:       },
200:       {
201:         id: "discover-clue-a",
202:         presenterLabel: "Encontrar la pista del jardín · yo",
203:         activityPresentation: {
204:           title: "Pista del jardín encontrada",
205:           description: "Hallazgo aportado por ti.",
206:         },
207:         expectedCheckpoint: "clue-a-discovered",
208:         action: {
209:           type: "scenario_action",
210:           actionId: "discover-clue-a",
211:           evidence: {
212:             id: "evidence-a-p1",
213:             type: "treasure_hunt.marker-a",
214:             occurredAt: "2026-09-12T10:00:00Z",
215:             source: "demo-control",
216:             reliability: "confirmed",
217:             subjects: [{ type: "individual", id: "subject-p1", role: "guest" }],
218:             contexts: [
219:               { type: "booking", id: "AS-8842" },
220:               { type: "stay", id: "stay-AS-8842" },
221:             ],
222:           },
223:         },
224:       },
225:       {
226:         id: "activate-p2",
227:         presenterLabel: "Activar al huésped 2 desde mi cuenta",
228:         expectedCheckpoint: "clue-a-discovered",
229:         action: {
230:           type: "scenario_action",
231:           actionId: "activate-p2",
232:           operation: "activate",
233:         },
234:       },
235:       {
236:         id: "discover-clue-b",
237:         presenterLabel: "Encontrar la pista de la fuente · huésped 2",
238:         activityPresentation: {
239:           title: "Pista de la fuente encontrada",
240:           description: "Hallazgo atribuido al huésped 2, registrado desde tu cuenta.",
241:         },
242:         expectedCheckpoint: "adventure-established",
243:         action: {
244:           type: "scenario_action",
245:           actionId: "discover-clue-b",
246:           evidence: {
247:             id: "evidence-b-p2",
248:             type: "treasure_hunt.marker-b",
249:             occurredAt: "2026-09-12T10:05:00Z",
250:             source: "demo-control",
251:             reliability: "confirmed",
252:             subjects: [{ type: "individual", id: "subject-p2", role: "guest" }],
253:             contexts: [
254:               { type: "booking", id: "AS-8842" },
255:               { type: "stay", id: "stay-AS-8842" },
256:             ],
257:           },
258:         },
259:       },
260:     ],
261:   },
262: };
```

## src/demo-factory/costa-artifacts.ts
SHA256 19b8dbb4571268a4513251212616d19bba324d0f8764eaed74ccb598864cb97c
```text
5: export const costaBrand: BrandArtifact = {
6:   id: "costa-clara",
7:   name: "Costa Clara Resort",
8:   logoUrl: costaLogoUrl,
```
```text
29: export const costaScenario: ScenarioDefinition = {
30:     id: "family-adventure-costa",
31:     experienceRef: "experience:family-adventure@1",
32:     subjects: [
33:       { type: "individual", id: "subject-p1", role: "guest" },
34:       { type: "individual", id: "subject-p2", role: "guest" },
35:     ],
36:     contexts: [
37:       { type: "property", id: "costa-clara-resort" },
38:       { type: "booking", id: "CC-205" },
39:       { type: "stay", id: "stay-CC-205" },
40:     ],
41:     checkpoints: ["ready", "clue-a-discovered", "adventure-established"],
42:     initialCheckpoint: "ready",
43:     operationalSessionSubjectRef: "subject-p1",
44:     initialSubjectStates: { "subject-p1": "not-enlisted", "subject-p2": "not-enabled" },
45:     presenterAction: {
46:       actionId: "enlist-p1",
47:       fromCheckpoint: "ready",
48:       toCheckpoint: "ready",
49:     },
50:     actions: [
51:       {
52:         actionId: "enlist-p1",
53:         fromCheckpoint: "ready",
54:         toCheckpoint: "ready",
55:         kind: "enlist",
56:         subjectRef: "subject-p1",
57:       },
58:       {
59:         actionId: "discover-clue-a",
60:         fromCheckpoint: "ready",
61:         toCheckpoint: "clue-a-discovered",
62:         kind: "evidence",
63:         subjectRef: "subject-p1",
64:         requiresEnabledSubject: true,
65:         evidenceType: "treasure_hunt.marker-a",
66:       },
67:       {
68:         actionId: "activate-p2",
69:         fromCheckpoint: "clue-a-discovered",
70:         toCheckpoint: "clue-a-discovered",
71:         kind: "activate",
72:         subjectRef: "subject-p2",
73:       },
74:       {
75:         actionId: "discover-clue-b",
76:         fromCheckpoint: "clue-a-discovered",
77:         toCheckpoint: "adventure-established",
78:         kind: "evidence",
79:         subjectRef: "subject-p2",
80:         requiresEnabledSubject: true,
81:         evidenceType: "treasure_hunt.marker-b",
82:       },
83:     ],
84:   };
```
```text
86: export const costaScript: DemoScript = {
87:     id: "family-adventure-costa",
88:     scenarioRef: "scenario:family-adventure-costa@1",
89:     initialCheckpoint: "ready",
90:     experimentalIntroductoryFraming: "Una aventura de pistas entre el mirador y el patio.",
91:     subjectPresentations: [
92:       { subjectRef: "subject-p1", label: "Inés" },
93:       { subjectRef: "subject-p2", label: "Mateo" },
94:     ],
95:     experimentalJourneyPresentations: [
96:       { availableActionId: "discover-clue-a", message: "Exploración disponible en el mirador." },
97:       { availableActionId: "activate-p2", message: "Pista del mirador registrada. La siguiente acción está disponible." },
98:       { availableActionId: "discover-clue-b", message: "Nueva exploración disponible en el patio." },
99:     ],
100:     steps: [
101:       {
102:         id: "enlist-p1",
103:         presenterLabel: "Alistarme",
104:         expectedCheckpoint: "ready",
105:         action: {
106:           type: "scenario_action",
107:           actionId: "enlist-p1",
108:           operation: "enlist",
109:         },
110:       },
111:       {
112:         id: "discover-clue-a",
113:         presenterLabel: "Encontrar la pista del mirador · Inés",
114:         activityPresentation: {
115:           title: "Pista del mirador encontrada",
116:           description: "Hallazgo aportado por Inés.",
117:         },
118:         expectedCheckpoint: "clue-a-discovered",
119:         action: {
120:           type: "scenario_action",
121:           actionId: "discover-clue-a",
122:           evidence: {
123:             id: "evidence-costa-a-p1",
124:             type: "treasure_hunt.marker-a",
125:             occurredAt: "2026-09-12T10:00:00Z",
126:             source: "demo-control",
127:             reliability: "confirmed",
128:             subjects: [{ type: "individual", id: "subject-p1", role: "guest" }],
129:             contexts: [
130:               { type: "booking", id: "CC-205" },
131:               { type: "stay", id: "stay-CC-205" },
132:             ],
133:           },
134:         },
135:       },
136:       {
137:         id: "activate-p2",
138:         presenterLabel: "Activar a Mateo desde mi cuenta",
139:         expectedCheckpoint: "clue-a-discovered",
140:         action: {
141:           type: "scenario_action",
142:           actionId: "activate-p2",
143:           operation: "activate",
144:         },
145:       },
146:       {
147:         id: "discover-clue-b",
148:         presenterLabel: "Encontrar la pista del patio · Mateo",
149:         activityPresentation: {
150:           title: "Pista del patio encontrada",
151:           description: "Hallazgo atribuido a Mateo, registrado desde la cuenta de Inés.",
152:         },
153:         expectedCheckpoint: "adventure-established",
154:         action: {
155:           type: "scenario_action",
156:           actionId: "discover-clue-b",
157:           evidence: {
158:             id: "evidence-costa-b-p2",
159:             type: "treasure_hunt.marker-b",
160:             occurredAt: "2026-09-12T10:05:00Z",
161:             source: "demo-control",
162:             reliability: "confirmed",
163:             subjects: [{ type: "individual", id: "subject-p2", role: "guest" }],
164:             contexts: [
165:               { type: "booking", id: "CC-205" },
166:               { type: "stay", id: "stay-CC-205" },
167:             ],
168:           },
169:         },
170:       },
171:     ],
172:   };
```

## src/demo-factory/fixtures.ts
SHA256 c855079b5601705b243c01bcfc11f54a41f58834bb83e9c558585c4ed820b791
```text
83: export const hospitalityFixture: DemoFixture = {
84:   id: "fixture:hospitality-stay@1",
85:   member: {
86:     id: "guest-lucia-vega",
87:     name: "Lucía",
88:     fullName: "Lucía Vega",
89:     initials: "LV",
90:     level: "Voyager",
91:     nextLevel: "Luminary",
92:     points: 3_480,
93:     progress: 48,
94:     pointsToNextLevel: 520,
95:     memberSince: "enero de 2025",
96:   },
97:   coupons: [
98:     {
```
```text
145: // Situated input only: no pre-enablement, Evidence, admissibility or claim.
146: export const costaFixture: DemoFixture = {
147:   id: "fixture:family-adventure-costa@1",
148:   member: {
149:     id: "guest-ines-costa",
150:     name: "Inés",
151:     fullName: "Inés Costa",
152:     initials: "IC",
153:     level: "Voyager",
154:     nextLevel: "Luminary",
155:     points: 3480,
156:     progress: 48,
157:     pointsToNextLevel: 520,
158:     memberSince: "enero de 2025",
159:   },
160:   coupons: [{
```

## src/demo-factory/bootstrap.ts
SHA256 6388ada8fde7ea4b043d6f5c75f8fa925f213499350ffd6f0dd038e7caa1cd54
```text
100: ): ResolvedDemoRuntime {
101:   const manifest = catalogs.manifests[demoId];
102:   if (!manifest) {
103:     throw new Error(`Demo desconocida: "${demoId}".`);
104:   }
105:   if (manifest.schemaVersion !== 1) {
106:     throw new Error(`Demo "${demoId}": schemaVersion incompatible.`);
107:   }
108: 
109:   const brand = requiredArtifact(
110:     catalogs.brands,
111:     manifest.brandRef,
112:     "marca",
113:     demoId,
114:   );
115:   validateBrand(brand, demoId);
116:   const fixture = requiredArtifact(
117:     catalogs.fixtures,
118:     manifest.fixtureRef,
119:     "fixture",
120:     demoId,
121:   );
122: 
123:   const scenario = manifest.scenarioRef
124:     ? requiredArtifact(catalogs.scenarios, manifest.scenarioRef, "Scenario", demoId)
125:     : undefined;
126:   const experience = scenario
127:     ? requiredArtifact(
128:         catalogs.experiences,
129:         scenario.experienceRef,
130:         "Experience",
131:         demoId,
132:       )
133:     : undefined;
134:   const script = manifest.scriptRef
135:     ? requiredArtifact(catalogs.scripts, manifest.scriptRef, "Demo Script", demoId)
136:     : undefined;
137: 
138:   if (script && (!scenario || script.scenarioRef !== manifest.scenarioRef)) {
139:     throw new Error(`Demo "${demoId}": Demo Script incompatible con Scenario.`);
140:   }
141:   if (script && !scenario?.checkpoints.includes(script.initialCheckpoint)) {
142:     throw new Error(`Demo "${demoId}": checkpoint inicial no resuelto.`);
143:   }
144:   if (scenario && !scenario.checkpoints.includes(scenario.initialCheckpoint)) {
145:     throw new Error(`Demo "${demoId}": checkpoint inicial de Scenario no resuelto.`);
146:   }
147:   const scriptStep = script?.steps[0];
148:   if (
149:     scriptStep &&
150:     scenario &&
151:     (scriptStep.action.actionId !== scenario.presenterAction.actionId ||
152:       scriptStep.expectedCheckpoint !== scenario.presenterAction.toCheckpoint)
153:   ) {
154:     throw new Error(`Demo "${demoId}": acción o checkpoint esperado incompatibles.`);
155:   }
156: 
157:   return {
158:     manifest,
159:     brand,
160:     experience,
161:     scenario,
162:     script,
163:     provider: new MockDataAdapter(fixture, scenario, script, experience?.name),
164:     capabilities: resolveCapabilities(manifest),
165:   };
```

## src/demo/mock-adapter.ts
SHA256 6e688118327e9f36ee55c23b6d100409e4f7cb01f668ad2152a5bde2c6912b35
```text
32: function formatActivityDate(occurredAt: string): string {
33:   return new Intl.DateTimeFormat("es-ES", {
34:     day: "numeric",
35:     month: "short",
36:     hour: "2-digit",
37:     minute: "2-digit",
38:     timeZone: "UTC",
39:   }).format(new Date(occurredAt));
40: }
41: 
42: export function projectSnapshot(
43:   fixture: DemoFixture,
44:   scenario?: ScenarioDefinition,
45:   checkpoint?: string,
46:   evaluation: VerticalEvaluationState = { evidence: [], jointAdmissibility: "cannot-currently-establish", sufficiency: "not-attempted" },
47:   subjectStates: Record<string, DemoSubjectState> = {},
48:   subjectPresentations: DemoScript["subjectPresentations"] = [],
49:   experimentalJourneyPresentations: DemoScript["experimentalJourneyPresentations"] = [],
50:   experienceName = "",
51: ): AppSnapshot {
52:   const snapshot: AppSnapshot = {
53:     member: structuredClone(fixture.member),
54:     coupons: structuredClone(fixture.coupons),
55:     news: structuredClone(fixture.news),
56:     activity: fixture.activityRecords.map((record) => ({
57:       id: record.id,
58:       title: record.title,
59:       description: record.description,
60:       occurredAt: record.occurredAt,
61:       displayDate: formatActivityDate(record.occurredAt),
62:       points: record.points,
63:       provenance: record.provenance,
64:       ...visualByKind[record.kind],
65:     })),
66:   };
67: 
68:   if (scenario && checkpoint) {
69:     const configuredAction = scenario.actions?.find((action) =>
70:       action.fromCheckpoint === checkpoint &&
71:       (!action.subjectRef || (action.kind === "enlist"
72:         ? subjectStates[action.subjectRef] === "not-enlisted"
73:         : action.kind === "activate"
74:           ? subjectStates[action.subjectRef] === "not-enabled" && subjectStates[scenario.operationalSessionSubjectRef ?? ""] === "enabled"
75:           : !action.requiresEnabledSubject || subjectStates[action.subjectRef] === "enabled")),
76:     );
77:     snapshot.scenario = {
78:       checkpoint,
79:       availableActionId: scenario.actions
80:         ? configuredAction?.actionId
81:         : checkpoint === scenario.presenterAction.fromCheckpoint ? scenario.presenterAction.actionId : undefined,
82:     };
83:   }
84: 
85:   if (scenario?.experienceRef === "experience:family-adventure@1") {
86:     snapshot.guestPerspective = projectGuestPerspective(
87:       evaluation, scenario.subjects, subjectStates, subjectPresentations, fixture.member.name,
88:       snapshot.scenario?.availableActionId, experimentalJourneyPresentations, experienceName,
89:     );
90:     snapshot.supervisionPerspective = projectSupervisionPerspective(
91:       evaluation, scenario.subjects, subjectStates, scenario.operationalSessionSubjectRef,
92:     );
93:   }
94: 
95:   return snapshot;
96: }
```
```text
98: export class MockDataAdapter implements DemoProvider {
99:   readonly mode = "mock" as const;
100:   private readonly initialFixture: DemoFixture;
101:   private fixture: DemoFixture;
102:   private readonly scenario?: ScenarioDefinition;
103:   // H25 presentation dependency only; Scenario and public action still govern acceptance.
104:   private readonly script?: DemoScript;
105:   private checkpoint?: string;
106:   private evidence: DemoAction["evidence"][] = [];
107:   private subjectStates: Record<string, DemoSubjectState> = {};
108:   private evaluation = evaluateVerticalEvidence([]);
109: 
110:   constructor(fixture: DemoFixture, scenario?: ScenarioDefinition, script?: DemoScript, private readonly experienceName = "") {
111:     this.initialFixture = structuredClone(fixture);
112:     this.fixture = structuredClone(fixture);
113:     this.scenario = scenario ? structuredClone(scenario) : undefined;
114:     this.script = script ? structuredClone(script) : undefined;
115:     this.checkpoint = scenario?.initialCheckpoint;
116:     this.subjectStates = structuredClone(scenario?.initialSubjectStates ?? {});
117:   }
118: 
119:   async getSnapshot(): Promise<AppSnapshot> {
120:     return projectSnapshot(
121:       this.fixture,
122:       this.scenario,
123:       this.checkpoint,
124:       this.evaluation,
125:       this.subjectStates,
126:       this.script?.subjectPresentations,
127:       this.script?.experimentalJourneyPresentations,
128:       this.experienceName,
129:     );
130:   }
131: 
132:   async executeAction(action: DemoAction | DemoEnableAction): Promise<AppSnapshot> {
133:     const transition = this.scenario?.actions?.find(
134:       ({ actionId }) => actionId === action.actionId,
135:     ) ?? this.scenario?.presenterAction;
136:     if (!transition || action.actionId !== transition.actionId) {
137:       throw new Error(`Acción de Scenario no permitida: ${action.actionId}.`);
138:     }
139:     if (this.checkpoint !== transition.fromCheckpoint) {
140:       throw new Error(
141:         `Acción ${action.actionId} no permitida desde checkpoint ${this.checkpoint ?? "ausente"}.`,
142:       );
143:     }
144: 
145:     const configuredAction = this.scenario?.actions?.find(
146:       ({ actionId }) => actionId === action.actionId,
147:     );
148:     const subjectRef = configuredAction?.subjectRef;
149:     if (configuredAction?.kind === "enlist" || configuredAction?.kind === "activate") {
150:       const expectedState = configuredAction.kind === "enlist" ? "not-enlisted" : "not-enabled";
151:       if (!subjectRef || !this.scenario?.subjects.some(({ id }) => id === subjectRef) || this.subjectStates[subjectRef] !== expectedState) {
152:         throw new Error(`Habilitación no permitida para sujeto ${subjectRef ?? "ausente"}.`);
153:       }
154:       if (!("operation" in action) || action.operation !== configuredAction.kind || "evidence" in action) {
155:         throw new Error("El alistamiento y la activación no producen Evidence.");
156:       }
157:       const sessionSubject = this.scenario.operationalSessionSubjectRef;
158:       if (!sessionSubject || (configuredAction.kind === "enlist"
159:         ? sessionSubject !== subjectRef
160:         : this.subjectStates[sessionSubject] !== "enabled" || sessionSubject === subjectRef)) {
161:         throw new Error("La operación requiere la sesión de P1 habilitada.");
162:       }
163:       this.subjectStates[subjectRef] = "enabled";
164:     } else {
165:       if (!("evidence" in action) || "operation" in action) {
166:         throw new Error("La acción de exploración requiere Evidence.");
167:       }
168:       const { evidence } = action;
169:       if (configuredAction?.requiresEnabledSubject) {
170:         if (!subjectRef || this.subjectStates[subjectRef] !== "enabled") {
171:           throw new Error(`El sujeto ${subjectRef ?? "ausente"} aún no está habilitado.`);
172:         }
173:         if (evidence.subjects.length !== 1 || evidence.subjects[0].id !== subjectRef || evidence.subjects[0].type !== "individual" || evidence.type !== configuredAction.evidenceType || evidence.interpretation) {
174:           throw new Error("Evidence incompatible con la acción y su atribución configurada.");
175:         }
176:       }
177:       this.evidence.push(structuredClone(evidence));
178:       if (this.scenario?.experienceRef === "experience:family-adventure@1") this.evaluation = evaluateVerticalEvidence(this.evidence, this.scenario.contexts);
179:       // H25 local experimental absence behavior, not a product fallback policy:
180:       // an accepted enabled-subject Evidence action without presentation adds no
181:       // situated Activity record. Generic Activity retains its existing behavior.
182:       const presentation = configuredAction?.requiresEnabledSubject
183:         ? this.script?.steps.find((step) => step.action.actionId === action.actionId)?.activityPresentation
184:         : { title: evidence.type, description: `Evidencia recibida desde ${evidence.source}.` };
185:       if (presentation) this.fixture.activityRecords.unshift({
186:         id: evidence.id,
187:         kind: "evidence",
188:         title: presentation.title,
189:         description: presentation.description,
190:         occurredAt: evidence.occurredAt,
191:         provenance: "simulated",
192:       });
193:     }
194:     this.checkpoint = transition.toCheckpoint;
195:     return this.getSnapshot();
196:   }
197: 
198:   async reset(): Promise<AppSnapshot> {
199:     this.fixture = structuredClone(this.initialFixture);
200:     this.checkpoint = this.scenario?.initialCheckpoint;
201:     this.evidence = [];
202:     this.subjectStates = structuredClone(this.scenario?.initialSubjectStates ?? {});
203:     this.evaluation = evaluateVerticalEvidence([]);
204:     return this.getSnapshot();
205:   }
```

## src/demo-factory/vertical-evaluation.ts
SHA256 e021823511336bfa31699120bb3ed9d039362ea97b787a155b89c895328891fd
```text
63: export function evaluateVerticalEvidence(
64:   evidence: readonly EvidenceInput[],
65:   situatedContexts: readonly ContextReference[] = [],
66: ): VerticalEvaluationState {
67:   const unavailable: VerticalEvaluationState = {
68:     evidence,
69:     jointAdmissibility: "cannot-currently-establish",
70:     sufficiency: "not-attempted",
71:   };
72:   if (evidence.length === 0) return unavailable;
73: 
74:   const propertyRef = contextReference(situatedContexts, "property");
75:   const bookingRef = contextReference(situatedContexts, "booking");
76:   const stayRef = contextReference(situatedContexts, "stay");
77:   if (!propertyRef || !bookingRef || !stayRef) return unavailable;
78: 
79:   const evaluationContext: CrossSubjectEvaluationContext = {
80:     evaluationRef: "evaluation-family-adventure-1",
81:     huntRef: "hunt-family-adventure-1",
82:     propertyRef, bookingRef, stayRef,
83:   };
84:   const converted: CrossSubjectMarkerEvidence[] = [];
85:   for (const item of evidence) {
86:     const input = toCrossSubjectEvidence(item, evaluationContext);
87:     if (!input) return unavailable;
88:     converted.push(input);
89:   }
90:   const criterion: TreasureHuntSufficiencyCriterion = {
91:     criterionRef: "criterion-family-adventure",
92:     authorityRef: "scenario-policy:family-adventure@1",
93:     scope: { huntRef: evaluationContext.huntRef, propertyRef },
94:     anchorMarkerRef: "marker-a",
95:     alternativeMarkerRefs: ["marker-b", "marker-c"],
96:   };
97:   // Existing experimental premise, explicitly assumed for this situated run.
98:   // Its authority and fixed P1/P2 coverage are not inferred from Evidence or
99:   // context equality. H17 still checks applicability separately before K.
100:   const authoritativePremise: AuthoritativePremise = {
101:     premiseRef: "premise-family-adventure-p1-p2@1",
102:     authorityRef: "fixture-policy:resort-family-adventure@1",
103:     scope: evaluationContext,
104:     coveredSubjectRefs: ["subject-p1", "subject-p2"],
105:   };
106: 
107:   const outcome = evaluateCrossSubjectEvidenceSufficiency(
108:     converted,
109:     evaluationContext,
110:     criterion,
111:     authoritativePremise,
112:   );
113: 
114:   if (!outcome.sufficiency.attempted) {
115:     return {
116:       evidence,
117:       jointAdmissibility: outcome.jointAdmissibility.determination,
118:       sufficiency: "not-attempted",
119:     };
120:   }
121: 
122:   return {
123:     evidence,
124:     jointAdmissibility: outcome.jointAdmissibility.determination,
125:     sufficiency: outcome.sufficiency.claim.determination,
126:     claim: outcome.sufficiency.claim,
127:   };
128: }
129: 
130: export function projectGuestPerspective(
131:   evaluation: VerticalEvaluationState,
132:   subjects: readonly SubjectReference[] = [],
133:   subjectStates: Record<string, DemoSubjectState> = {},
134:   subjectPresentations: DemoScript["subjectPresentations"] = [],
135:   // H28: existing account display source only, never subject/viewer identity.
136:   accountName = "",
137:   availableActionId?: string,
138:   experimentalJourneyPresentations: DemoScript["experimentalJourneyPresentations"] = [],
139:   // H35: resolved Experience.name; semantic name transport, not Script copy.
140:   experienceName = "",
141: ): GuestPerspectiveReadModel {
142:   const discoveredClueCount = evaluation.evidence.length;
143:   const complete = evaluation.sufficiency === "established";
144:   const enlisted = subjectStates["subject-p1"] === "enabled";
145:   return {
146:     huntName: experienceName,
147:     sessionLabel: `Cuenta de ${accountName}`,
148:     subjects: subjects.map(({ id }) => ({
149:       id,
150:       // H27 local absence: no supplied label means no display text. The subject
151:       // still comes from Scenario; this is not a general product fallback policy.
152:       label: subjectPresentations.find(({ subjectRef }) => subjectRef === id)?.label ?? "",
153:       // H29: present operational state only; no actor, viewer or personal gender.
154:       status: ({
155:         "not-enlisted": "Estado: sin alistar",
156:         "not-enabled": "Estado: sin habilitar",
157:         enabled: "Estado: habilitado",
158:       })[subjectStates[id]] ?? "",
159:       clueCount: evaluation.evidence.filter((item) => item.subjects.some((subject) => subject.id === id)).length,
160:     })),
161:     state: complete ? "complete" : discoveredClueCount > 0 ? "exploring" : enlisted ? "active" : "ready",
162:     message: complete
163:       ? "Las pistas aportadas cumplen la condición de esta aventura."
164:       : discoveredClueCount === 0 && subjectStates["subject-p1"] === "not-enlisted"
165:         ? "La aventura está disponible. Alistamiento pendiente."
166:         // H30 local presentation lookup only. Missing affordance/declaration
167:         // means no situated copy; absence is not a product UX policy.
168:         : availableActionId
169:           ? experimentalJourneyPresentations.find((item) => item.availableActionId === availableActionId)?.message ?? ""
170:           : "",
171:     discoveredClueCount,
172:   };
173: }
174: 
175: export function projectSupervisionPerspective(
176:   evaluation: VerticalEvaluationState,
177:   subjects: readonly SubjectReference[] = [],
178:   subjectStates: Record<string, DemoSubjectState> = {},
179:   sessionSubjectRef?: string,
180: ): SupervisionPerspectiveReadModel {
181:   return {
182:     sessionSubjectRef,
183:     subjects: subjects.map(({ id }) => ({
184:       id,
185:       exists: true,
186:       operationalState: subjectStates[id] ?? "not-enabled",
187:       evidenceCount: evaluation.evidence.filter((item) => item.subjects.some((subject) => subject.id === id)).length,
188:     })),
189:     evidence: evaluation.evidence.map((item) => ({
190:       id: item.id,
191:       subjectRefs: item.subjects.map(({ id }) => id),
192:       type: item.type,
193:       provenance: item.source,
194:     })),
195:     jointAdmissibility: evaluation.jointAdmissibility,
196:     sufficiency: evaluation.sufficiency,
197:     derivedClaim: evaluation.claim?.determination ?? "not-produced",
198:   };
199: }
```

## src/app/App.tsx
SHA256 cde3b490f05d42bf11abff185f09b9be5e8828897cc0a96a1c064a964a99b8ef
```text
62:   if (items.length === 0) {
63:     return (
64:       <FeedbackState
65:         icon="activity"
66:         title="Aún no hay actividad"
67:         description="Tus movimientos y novedades aparecerán aquí."
68:       />
69:     );
70:   }
71: 
72:   return (
73:     <div className={`activity-list${compact ? " activity-list--compact" : ""}`}>
74:       {items.map((item) => (
75:         <article className="activity-item" key={item.id}>
76:           <span className={`activity-item__icon activity-item__icon--${item.tone}`} aria-hidden="true">
77:             <Icon name={item.icon} size={20} />
78:           </span>
79:           <div className="activity-item__content">
80:             <div className="activity-item__heading">
81:               <h3>{item.title}</h3>
82:               {item.points !== undefined && (
83:                 <strong className={item.points >= 0 ? "points-positive" : ""}>
84:                   {item.points >= 0 ? "+" : ""}{item.points} pts
85:                 </strong>
86:               )}
87:             </div>
88:             <p>{item.description}</p>
89:             <time dateTime={item.occurredAt}>{item.displayDate}</time>
90:           </div>
91:         </article>
92:       ))}
93:     </div>
94:   );
95: }
96: 
97: function HomePage({
98:   snapshot,
99:   guestAction,
100:   guestActionLabel,
101:   brandName,
102:   introductoryFraming,
103: }: {
104:   snapshot: AppSnapshot;
105:   guestAction: () => void;
106:   guestActionLabel?: string;
107:   brandName: ResolvedDemoRuntime["brand"]["name"];
108:   introductoryFraming?: string;
109: }) {
110:   const { member, coupons, activity, news } = snapshot;
111: 
112:   if (snapshot.guestPerspective) {
113:     const adventure = snapshot.guestPerspective;
114:     return (
115:       <main id="main-content" className="adventure-page">
116:         <header className="adventure-heading">
117:           <p className="eyebrow">Mi aventura · {brandName}</p>
118:           <h1 id="adventure-title">{adventure.huntName}</h1>
119:           {introductoryFraming && <p>{introductoryFraming}</p>}
120:         </header>
121:         <section className="adventure-next" aria-labelledby="next-action-title">
122:           <p className="eyebrow" id="next-action-title">{guestActionLabel ? "Tu siguiente paso" : "Resultado de la aventura"}</p>
123:           <p className="adventure-message" role="status">{adventure.message}</p>
124:           {guestActionLabel && <button className="secondary-action" type="button" onClick={guestAction}>{guestActionLabel}<Icon name="arrow" size={18} /></button>}
125:           <p className="adventure-count">{adventure.discoveredClueCount} {adventure.discoveredClueCount === 1 ? "pista descubierta" : "pistas descubiertas"}</p>
126:         </section>
127:         <section aria-labelledby="guests-title">
128:           <h2 id="guests-title">Quién puede explorar</h2>
129:           <div className="adventure-guests">
130:             {adventure.subjects.map((subject) => (
131:               <article className="adventure-guest" key={subject.id}>
132:                 <h3>{subject.label}</h3>
133:                 <p>{subject.status} · {subject.clueCount} {subject.clueCount === 1 ? "pista aportada" : "pistas aportadas"}</p>
134:               </article>
135:             ))}
136:           </div>
137:           <p className="adventure-session">{adventure.sessionLabel}</p>
138:         </section>
139:       </main>
140:     );
```
```text
247: function ActivityPage({ activity }: { activity: ActivityItem[] }) {
248:   return (
249:     <main id="main-content" className="page-stack">
250:       <header className="page-header">
251:         <p className="eyebrow">Todo al día</p>
252:         <h1>Actividad</h1>
253:         <p>Consulta tus puntos, beneficios y últimas interacciones.</p>
254:       </header>
255:       <section aria-labelledby="activity-list-title">
256:         <h2 className="section-title" id="activity-list-title">Últimos movimientos</h2>
257:         <ActivityList items={activity} />
258:       </section>
259:     </main>
260:   );
```
```text
348:   if (snapshot.supervisionPerspective) {
349:     const supervision = snapshot.supervisionPerspective;
350:     return (
351:       <main id="main-content" className="adventure-page">
352:         <header className="adventure-heading">
353:           <p className="eyebrow">Supervisión</p>
354:           <h1 id="supervision-title">Estado de la aventura</h1>
355:           <p>Observa lo que cambia al actuar en «Mi aventura». Cambiar de vista conserva la sesión.</p>
356:         </header>
357:         <section className="adventure-guests" aria-label="Sujetos existentes">
358:           {supervision.subjects.map((subject) => (
359:             <article className="adventure-guest" key={subject.id}>
360:               <h2>{subject.id}</h2>
361:               <p>{subject.id} · exists: {String(subject.exists)} · {subject.operationalState} · Evidence: {subject.evidenceCount}</p>
362:             </article>
363:           ))}
364:         </section>
365:         <section className="system-panel" aria-label="Evaluación compartida">
366:           <dl className="system-list">
367:             <div><dt>Sujeto de sesión operativa</dt><dd>{supervision.sessionSubjectRef}</dd></div>
368:             <div><dt>Criterio K</dt><dd>A AND (B OR C)</dd></div>
369:             <div><dt>Evidence recibida</dt><dd>{supervision.evidence.length}</dd></div>
370:             <div><dt>Admisibilidad conjunta</dt><dd>{supervision.jointAdmissibility}</dd></div>
371:             <div><dt>Suficiencia K</dt><dd>{supervision.sufficiency}</dd></div>
372:             <div><dt>Afirmación derivada</dt><dd>{supervision.derivedClaim}</dd></div>
373:           </dl>
374:         </section>
375:         <section aria-labelledby="evidence-title">
376:           <h2 id="evidence-title">Evidence y atribución</h2>
377:           {supervision.evidence.length === 0 ? <p>Todavía no hay Evidence. Alistarse o activar a un huésped no aporta pistas.</p> : (
378:             <ul className="adventure-evidence">{supervision.evidence.map((item) => <li key={item.id}>{item.id} · {item.subjectRefs.join(", ")} · {item.provenance}</li>)}</ul>
379:           )}
```
```text
450:   onPresenterAction: () => void;
451:   onReset: () => void;
452: }) {
453:   const guestActionLabel = runtime.script?.steps.find(({ action }) => action.actionId === snapshot.scenario?.availableActionId)?.presenterLabel;
454:   const isAdventure = Boolean(snapshot.guestPerspective);
455:   const demoSearch = `?demo=${runtime.manifest.demoId}`;
456:   return (
457:     <div className={`app-shell${isAdventure ? " app-shell--adventure" : ""}`}>
458:       <a className="skip-link" href="#main-content">Saltar al contenido</a>
459:       <header className="topbar">
460:         <Link to={`/${demoSearch}`} aria-label="Ir al inicio">
461:           <img
462:             className="brand-logo"
463:             src={runtime.brand.logoUrl}
464:             alt={runtime.brand.name}
465:           />
466:         </Link>
467:         {isAdventure ? <span className="adventure-account">Cuenta de {snapshot.member.name}</span> : (
468:           <Link className="profile-avatar" to="/profile" aria-label="Abrir perfil">{snapshot.member.initials}</Link>
469:         )}
470:       </header>
471: 
472:       {isAdventure && (
473:         <>
474:           <nav className="adventure-nav" aria-label="Navegación de la aventura">
475:             <NavLink to={`/${demoSearch}`} end>Mi aventura</NavLink>
476:             <NavLink to={`/activity${demoSearch}`}>Actividad</NavLink>
477:             <NavLink to={`/system${demoSearch}`}>Supervisión</NavLink>
478:           </nav>
479:           {actionError && <p className="adventure-error" role="alert">{actionError}</p>}
480:         </>
481:       )}
482:       <Routes>
483:         <Route path="/" element={<HomePage snapshot={snapshot} guestAction={onPresenterAction} guestActionLabel={guestActionLabel} brandName={runtime.brand.name} introductoryFraming={runtime.script?.experimentalIntroductoryFraming} />} />
```
```text
540:   const runPresenterAction = async () => {
541:     const step = runtime.script?.steps.find(
542:       ({ action }) => action.actionId === snapshot.scenario?.availableActionId,
543:     );
544:     if (!step) return;
545: 
546:     setActionError(undefined);
547:     try {
548:       setSnapshot(await runtime.provider.executeAction(step.action));
549:     } catch (actionFailure) {
550:       setActionError(
551:         actionFailure instanceof Error
552:           ? actionFailure.message
553:           : "No se pudo ejecutar la acción de presentación.",
554:       );
555:     }
556:   };
557: 
558:   return (
559:     <AppShell
560:       snapshot={snapshot}
561:       runtime={runtime}
562:       actionError={actionError}
563:       onPresenterAction={runPresenterAction}
564:       onReset={async () => {
565:         setActionError(undefined);
566:         try {
567:           setSnapshot(await runtime.provider.reset());
568:           document.getElementById("main-content")?.scrollIntoView?.({ block: "start" });
569:         }
570:         catch { setActionError("No se pudo reiniciar la aventura."); }
571:       }}
572:     />
573:   );
574: }
```
