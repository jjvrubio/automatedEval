import { useEffect, useRef, useState } from "react";
import type { SportsDemoAction, SportsSeasonResolvedRuntime, SportsSnapshot } from "@/demo-factory/sports-season/contracts";
import { Icon } from "@/ui/Icon";
import "../styles/sports-season.css";
import { SportsEquipmentPanel, SportsInterestPanel, SportsPersonPanel, SportsVoluntaryPanel, type SportsDrafts } from "./SportsUserPanels";
import { SportsSelfService } from "./SportsRelationshipPanels";
import { SportsSurface } from "./SportsSurface";

const emptyDrafts: SportsDrafts = { visitorName: "", interests: [], frequency: "", goal: "" };

function eventDate(date: string) {
  return new Intl.DateTimeFormat("es-ES", { day: "numeric", month: "long", timeZone: "UTC" }).format(new Date(date));
}

function CRMView({ snapshot }: { snapshot: SportsSnapshot }) {
  const { scenario, registration, evidence, badge, opportunity } = snapshot;
  const event = scenario.events.find((item) => item.id === registration?.eventRef);
  const modality = scenario.modalities.find((item) => item.value === registration?.selectedModality);
  return (
    <main id="sports-main" className="sports-main">
      <header className="sports-heading">
        <p className="sports-kicker">Marketing / CRM</p>
        <h1>La participación, con contexto.</h1>
        <p>La misma persona y los mismos registros.{scenario.person.membershipStatus === "external" ? " Una oportunidad para iniciar una relación con el club." : " Su pertenencia al club se mantiene."}</p>
      </header>
      <div className="sports-crm-grid">
        <section className="sports-panel" aria-labelledby="crm-person">
          <p className="sports-kicker">01 · Datos de escenario ficticio</p>
          <h2 id="crm-person">{scenario.person.name}</h2>
          <dl className="sports-facts">
            <div><dt>Estado de club</dt><dd>{scenario.person.membershipStatus === "member" ? "Miembro del club" : "Externo · no pertenece al club"}</dd></div>
            <div><dt>Relación como cliente</dt><dd>{scenario.person.customerRelationship === "established" ? "Cliente conocido" : "No establecida"}</dd></div>
            <div><dt>Temporada</dt><dd>{scenario.season.title}</dd></div>
            <div><dt>Periodo</dt><dd>{scenario.season.dates}</dd></div>
          </dl>
          <p className="sports-note">Persona y calendario proceden de datos ficticios. No hay autenticación real.</p>
        </section>
        <section className="sports-panel" aria-labelledby="crm-facts">
          <p className="sports-kicker">02 · Registros de esta ejecución</p>
          <h2 id="crm-facts">Inscripción y aportaciones</h2>
          {!registration ? <p>Todavía no se ha confirmado una inscripción.</p> : (
            <>
              <dl className="sports-facts">
                <div><dt>Evento</dt><dd>{event?.title}</dd></div>
                <div><dt>Disciplina</dt><dd>{event?.label}</dd></div>
                <div><dt>Modalidad elegida</dt><dd>{modality?.label}</dd></div>
                <div><dt>Inscripción</dt><dd>Aceptada · elección de esta participación</dd></div>
              </dl>
              <p className="sports-note">La inscripción no acredita presencia ni esfuerzo.</p>
            </>
          )}
          {evidence.length === 0 ? <p className="sports-empty">Sin evidencia de presencia o esfuerzo.</p> : (
            <ul className="sports-evidence">
              {evidence.map((item) => (
                <li key={item.evidenceId}>
                  <strong>{item.kind === "presence" ? "Presencia · check-in simulado" : `Esfuerzo · ${item.level}`}</strong>
                  <span>{item.kind === "presence" ? "Aceptada sólo dentro de la simulación. Sin acreditación física." : "Autodeclarado por el participante. Sin medición externa."}</span>
                  <small>Origen: {item.source} · <time dateTime={item.occurredAt}>{new Date(item.occurredAt).toLocaleTimeString("es-ES")}</time></small>
                </li>
              ))}
            </ul>
          )}
        </section>
        <section className="sports-panel" aria-labelledby="crm-badge">
          <p className="sports-kicker">03 · Reconocimiento derivado local</p>
          <h2 id="crm-badge">{badge ? badge.title : "Insignia pendiente"}</h2>
          <p>{badge ? badge.reason : snapshot.criterion.explanation}</p>
          <p className="sports-note">Los tres niveles de esfuerzo satisfacen el mismo requisito. No se infiere rendimiento ni intención de compra.</p>
          <details className="sports-details">
            <summary>Criterio y referencias</summary>
            <dl className="sports-facts sports-refs">
              <div><dt>Regla local experimental</dt><dd>{snapshot.criterion.ruleRef}</dd></div>
              <div><dt>Persona</dt><dd>{scenario.person.id}</dd></div>
              {registration && <div><dt>Inscripción / evento</dt><dd>{registration.registrationId} / {registration.eventRef}</dd></div>}
              {badge && <div><dt>Evidencias de apoyo</dt><dd>{badge.supportingEvidenceRefs.join(" · ")}</dd></div>}
            </dl>
          </details>
        </section>
        <section className="sports-panel sports-opportunity" aria-labelledby="crm-opportunity">
          <p className="sports-kicker">04 · Oportunidad comercial</p>
          <h2 id="crm-opportunity">{opportunity ? "Invitación al club disponible" : "Aún sin invitación"}</h2>
          <p>{opportunity ? `La participación de ${scenario.person.name} permite proponer conocer ${scenario.club.name}.` : scenario.person.membershipStatus === "member" ? "Ya pertenece al club. Esta participación no genera una invitación de alta." : "La invitación aparecerá después del reconocimiento de esta participación."}</p>
          <p>Estado de club: <strong>{scenario.person.membershipStatus === "member" ? "miembro" : "externo"}</strong>. Sin alta, consentimiento, conversión ni lead enviado.</p>
          <p className="sports-note">Continuidad registrada: {badge ? "primera participación reconocida en esta temporada." : "ninguna participación reconocida todavía."} No se ha ejecutado una segunda participación.</p>
        </section>
      </div>
      <details className="sports-contrast">
        <summary>Contraste de diseño · miembro y competición, sin ejecutar</summary>
        <p>{scenario.contrastPerson.name} ya pertenece al club en el escenario ficticio. En otro recorrido podría elegir competición y declarar resultado y posición para un reconocimiento individual; un trofeo sería distinto de una insignia o un beneficio. El recorrido competitivo no tiene acciones, resultados ni reconocimientos registrados.</p>
      </details>
    </main>
  );
}

export function SportsSeasonApp({ runtime, surface = "web" }: { runtime: SportsSeasonResolvedRuntime; surface?: "web" | "app" }) {
  const [snapshot, setSnapshot] = useState<SportsSnapshot>();
  const [view, setView] = useState<"participant" | "crm" | "self-service">("participant");
  const [selectedEvent, setSelectedEvent] = useState("");
  const [modality, setModality] = useState("");
  const [effort, setEffort] = useState("");
  const [clubOpen, setClubOpen] = useState(false);
  const [error, setError] = useState<string>();
  const [busy, setBusy] = useState(false);
  const [drafts, setDrafts] = useState<SportsDrafts>(emptyDrafts);
  const errorRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (error) errorRef.current?.focus();
  }, [error]);

  useEffect(() => {
    let mounted = true;
    runtime.provider.getSnapshot().then((value) => { if (mounted) setSnapshot(value); })
      .catch(() => { if (mounted) setError("No se ha podido cargar esta demo."); });
    return () => { mounted = false; };
  }, [runtime.provider]);

  async function run(action: SportsDemoAction) {
    setBusy(true);
    setError(undefined);
    try { setSnapshot(await runtime.provider.executeAction(action)); return true; }
    catch (failure) { setError(failure instanceof Error ? failure.message : "No se ha podido registrar la acción."); return false; }
    finally { setBusy(false); }
  }

  async function reset() {
    setBusy(true);
    setError(undefined);
    try {
      setSnapshot(await runtime.provider.reset());
      setSelectedEvent(""); setModality(""); setEffort(""); setClubOpen(false); setDrafts(emptyDrafts);
      setView("participant");
    } catch { setError("No se ha podido reiniciar la demo."); }
    finally { setBusy(false); }
  }

  if (!snapshot) return <main className="sports-main"><p role={error ? "alert" : "status"}>{error ?? "Preparando la temporada…"}</p></main>;
  const { scenario, registration, evidence, badge, opportunity } = snapshot;
  const user = snapshot.userPlane;
  const event = scenario.events.find((item) => item.id === (registration?.eventRef ?? user?.selectedEventRef ?? selectedEvent));
  const updateDrafts = (patch: Partial<SportsDrafts>) => setDrafts(value => ({ ...value, ...patch }));
  const choosePerson = async (personRef: string) => {
    if (personRef === user?.person?.id) return;
    if (await run({ type: "sports-select-person", personRef })) {
      setSelectedEvent(""); setModality(""); setEffort(""); setClubOpen(false); setDrafts(emptyDrafts);
    }
  };
  const panelProps = user ? { user, busy, run, drafts, update: updateDrafts } : undefined;
  const presence = evidence.find((item) => item.kind === "presence");
  const declaredEffort = evidence.find((item) => item.kind === "effort");
  const selectedModality = scenario.modalities.find((item) => item.value === registration?.selectedModality);
  const feedback = error ? <div ref={errorRef} className="sports-error" role="alert" tabIndex={-1}>{error}</div> : null;

  return (
    <SportsSurface surface={surface} demoId={runtime.manifest.demoId} brand={runtime.brand}>
    <div className="sports-shell">
      <a className="skip-link" href="#sports-main">Saltar al contenido</a>
      <header className="sports-topbar">
        <img src={runtime.brand.logoUrl} alt={runtime.brand.name} width="184" height="40" />
        <span className="sports-demo-label">Demo · marca y personas ficticias</span>
      </header>
      <nav className="sports-perspectives" aria-label="Perspectiva de la demo">
        <button type="button" aria-pressed={view === "participant"} onClick={() => setView("participant")}>Participante</button>
        <button type="button" aria-pressed={view === "self-service"} disabled={!user?.person || busy} onClick={() => setView("self-service")}>Self Service</button>
        <button type="button" aria-pressed={view === "crm"} disabled={Boolean(user && !user.person)} onClick={() => setView("crm")}>Marketing / CRM</button>
      </nav>
      {(view === "crm" || !event) && feedback}
      {view === "self-service" ? <SportsSelfService snapshot={snapshot} onEvent={() => setView("participant")} /> : view === "crm" ? <CRMView snapshot={snapshot} /> : (
        <main id="sports-main" className="sports-main">
          <header className="sports-hero">
            <div>
              <p className="sports-kicker">Temporada deportiva · {scenario.season.dates}</p>
              <h1>{scenario.season.title}</h1>
              <p>{scenario.season.introduction}</p>
              <span className="sports-tag">Abierta también a personas ajenas al club</span>
            </div>
            <div className="sports-track" aria-hidden="true"><span>Sal.<br />Muévete.<br /><em>Conecta.</em></span></div>
          </header>
          {panelProps ? <>
            <SportsPersonPanel {...panelProps} choosePerson={personRef => void choosePerson(personRef)} qrEventRef={scenario.events.find(item => item.executable)!.id} registered={Boolean(registration)} />
            <SportsInterestPanel {...panelProps} />
          </> : <div className="sports-person"><span className="sports-avatar" aria-hidden="true"><Icon name="user" /></span><div><strong>{scenario.person.name}</strong><span>Participante simulado · Externo al club</span></div><span className="sports-person-note">Participar no te da de alta.</span></div>}
          {user?.intention !== "information" && <>
          <section aria-labelledby="sports-events">
            <div className="sports-section-title"><div><p className="sports-kicker">Un programa, distintas formas de participar</p><h2 id="sports-events">Los eventos de la temporada</h2></div><span>3 disciplinas</span></div>
            <div className="sports-events">
              {scenario.events.map((item, index) => (
                <article className={`sports-event sports-event--${item.discipline}`} key={item.id}>
                  <div className="sports-event-top"><span className="sports-event-number">0{index + 1}</span><span className="sports-tag">{item.executable ? "Recorrido disponible" : "Sólo informativo"}</span></div>
                  <p className="sports-kicker">{item.label}</p><h3>{item.title}</h3>
                  <p className="sports-event-date"><time dateTime={item.date}>{eventDate(item.date)}</time> · {item.place}</p>
                  <p>{item.description}</p>
                  {item.executable ? <button className="sports-button sports-button--outline" type="button" disabled={Boolean(registration) || busy || Boolean(user && user.intention !== "participate")} onClick={() => { if (user) void run({ type: "sports-select-event", personRef: user.person!.id, eventRef: item.id }); else { setSelectedEvent(item.id); setError(undefined); } }}>
                    {registration ? "Inscripción confirmada" : (user?.selectedEventRef ?? selectedEvent) === item.id ? "Carrera seleccionada" : "Elegir Carrera"}<Icon name="arrow" size={18} />
                  </button> : <p className="sports-note">Sin inscripción disponible en esta demo.</p>}
                </article>
              ))}
            </div>
          </section>
          {user && <SportsEquipmentPanel user={user} />}
          {event && <section className="sports-journey" aria-labelledby="sports-journey-title">
            <div className="sports-journey-heading"><p className="sports-kicker">Tu participación · {event.label}</p><h2 id="sports-journey-title">{event.title}</h2></div>
            {!registration ? <form noValidate onSubmit={(e) => { e.preventDefault(); void run({ type: "sports-register", personRef: scenario.person.id, eventRef: event.id, selectedModality: modality }); }}>
              {user && <div className="sports-required-data"><p className="sports-kicker">Datos necesarios para inscribirse</p><p>Persona: <strong>{scenario.person.name}</strong> · Evento: <strong>{event.label}</strong>. Elige la modalidad; no necesitas aportar información adicional para participar.</p></div>}
              <fieldset disabled={busy}><legend>¿Cómo quieres participar esta vez?</legend>
                <div className="sports-options">{scenario.modalities.map((item) => <label key={item.value} className={`sports-option ${modality === item.value ? "is-selected" : ""}`}>
                  <input type="radio" name="modality" value={item.value} checked={modality === item.value} onChange={(e) => setModality(e.target.value)} />
                  <span><strong>{item.label}</strong><small>{item.description}</small></span>
                </label>)}</div>
              </fieldset>
              <p className="sports-note">La elección se aplica a este evento. No define tu perfil ni te incorpora al club.</p>
              <button className="sports-button" disabled={busy}>Confirmar inscripción<Icon name="arrow" size={18} /></button>
            </form> : (
              <div className="sports-steps">
                <div className="sports-step"><span className="sports-step-index">01</span><div><h3>Inscripción confirmada</h3><p>Modalidad {selectedModality?.label} · {scenario.person.name}</p></div><span className="sports-state">Registrada</span></div>
                {panelProps && <SportsVoluntaryPanel {...panelProps} />}
                <div className="sports-step"><span className="sports-step-index">02</span><div><h3>Registra tu presencia{user ? " · QR de presencia" : ""}</h3><p>{presence ? "Check-in simulado registrado. No acredita asistencia física real." : "Simula el check-in del evento. No se escanea un QR real ni se verifica asistencia física."}</p>
                  {!presence && <button className="sports-button" disabled={busy || Boolean(user && !user.voluntary)} onClick={() => void run({ type: "sports-check-in", personRef: scenario.person.id, eventRef: registration.eventRef, registrationRef: registration.registrationId })}>Simular check-in</button>}
                </div>{presence && <span className="sports-state">Simulada</span>}</div>
                <div className="sports-step"><span className="sports-step-index">03</span><div><h3>Comparte tu esfuerzo</h3>
                  {declaredEffort ? <p>Esfuerzo {declaredEffort.level} · autodeclarado, sin medición externa.</p> : presence ? <form noValidate onSubmit={(e) => { e.preventDefault(); void run({ type: "sports-effort", personRef: scenario.person.id, eventRef: registration.eventRef, registrationRef: registration.registrationId, level: effort }); }}>
                    <fieldset disabled={busy}><legend>¿Cómo has sentido el esfuerzo?</legend><div className="sports-efforts">{scenario.efforts.map((item) => <label key={item.value} className={effort === item.value ? "is-selected" : ""}><input type="radio" name="effort" value={item.value} checked={effort === item.value} onChange={(e) => setEffort(e.target.value)} />{item.label}</label>)}</div></fieldset>
                    <p className="sports-note">Es tu declaración, separada de la presencia. Los tres niveles reciben el mismo reconocimiento.</p>
                    <button className="sports-button" disabled={busy}>Registrar esfuerzo<Icon name="arrow" size={18} /></button>
                  </form> : <p>Disponible después del check-in simulado.</p>}
                </div>{declaredEffort && <span className="sports-state">Autodeclarado</span>}</div>
              </div>
            )}
            {feedback}
          </section>}
          {badge && <section className="sports-result" aria-labelledby="badge-title" role="status">
            <div className="sports-medallion" aria-hidden="true"><Icon name="star" size={46} /></div>
            <div><p className="sports-kicker">Tu insignia de Sports Season · Carrera</p><h2 id="badge-title">{badge.title}</h2><p>{badge.reason}</p><button type="button" className="sports-button" onClick={() => setView("self-service")}>Ver mi insignia en Self Service</button><p className="sports-note">Un reconocimiento individual de esta demo. No es un cupón, un trofeo ni un nivel del club.</p></div>
          </section>}
          {opportunity && <section className="sports-club" aria-labelledby="club-title">
            <div><p className="sports-kicker">Una invitación, una nueva decisión</p><h2 id="club-title">{scenario.club.invitation}</h2><p>{scenario.club.description}</p>
              <button className="sports-button" type="button" aria-expanded={clubOpen} onClick={() => setClubOpen(!clubOpen)}>{clubOpen ? "Cerrar información del club" : `Conocer ${scenario.club.name}`}<Icon name="arrow" size={18} /></button>
              {clubOpen && <div className="sports-club-info"><h3>{scenario.club.name}</h3><p>El club reúne novedades y próximas actividades de la marca. Esta pantalla sólo muestra información: sigues siendo participante externo. No se ha enviado una solicitud, un lead ni un consentimiento.</p></div>}
            </div>
            <aside><Icon name="compass" size={32} /><h3>La temporada continúa</h3><p>Esta es tu primera participación registrada. Vela y Vóley playa muestran otros encuentros del programa; sus recorridos aún no están disponibles en esta demo.</p></aside>
          </section>}
          </>}
        </main>
      )}
      <footer className="sports-footer"><p>Simulación local · Al recargar se reinicia la demo. Cambiar de perspectiva o de vista Web/App/Self Service conserva el recorrido.</p><button type="button" disabled={busy} onClick={() => void reset()}>Reiniciar demo</button></footer>
    </div>
    </SportsSurface>
  );
}
