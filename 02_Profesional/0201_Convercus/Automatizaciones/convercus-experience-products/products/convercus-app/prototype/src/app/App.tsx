import { useEffect, useState } from "react";
import { Link, NavLink, Route, Routes, useLocation } from "react-router-dom";
import { appConfig } from "@/config/app-config";
import { brand, brandAssets } from "@/config/brand";
import {
  MockDataAdapter,
  type ActivityItem,
  type AppSnapshot,
  type Coupon,
} from "@/demo/mock-adapter";
import { FeedbackState } from "@/ui/FeedbackState";
import { Icon, type IconName } from "@/ui/Icon";

const adapter = new MockDataAdapter();

function formatPoints(points: number): string {
  return new Intl.NumberFormat("es-ES").format(points);
}

function SectionHeading({
  eyebrow,
  title,
  linkTo,
}: {
  eyebrow?: string;
  title: string;
  linkTo?: string;
}) {
  return (
    <div className="section-heading">
      <div>
        {eyebrow && <p className="eyebrow">{eyebrow}</p>}
        <h2>{title}</h2>
      </div>
      {linkTo && (
        <Link className="text-link" to={linkTo}>
          Ver todo <Icon name="arrow" size={16} />
        </Link>
      )}
    </div>
  );
}

function CouponCard({ coupon, featured = false }: { coupon: Coupon; featured?: boolean }) {
  return (
    <article className={`coupon-card coupon-card--${coupon.tone}${featured ? " coupon-card--featured" : ""}`}>
      <div className="coupon-card__topline">
        <span className="coupon-card__icon" aria-hidden="true">
          <Icon name={coupon.icon} size={22} />
        </span>
        <span className="coupon-card__tag">{coupon.tag}</span>
      </div>
      <div>
        <h3>{coupon.title}</h3>
        <p>{coupon.description}</p>
      </div>
      <div className="coupon-card__footer">
        <span>{coupon.validUntil}</span>
        <span aria-hidden="true"><Icon name="arrow" size={18} /></span>
      </div>
    </article>
  );
}

function ActivityList({ items, compact = false }: { items: ActivityItem[]; compact?: boolean }) {
  if (items.length === 0) {
    return (
      <FeedbackState
        icon="activity"
        title="Aún no hay actividad"
        description="Tus movimientos y novedades aparecerán aquí."
      />
    );
  }

  return (
    <div className={`activity-list${compact ? " activity-list--compact" : ""}`}>
      {items.map((item) => (
        <article className="activity-item" key={item.id}>
          <span className={`activity-item__icon activity-item__icon--${item.tone}`} aria-hidden="true">
            <Icon name={item.icon} size={20} />
          </span>
          <div className="activity-item__content">
            <div className="activity-item__heading">
              <h3>{item.title}</h3>
              {item.points !== undefined && (
                <strong className={item.points >= 0 ? "points-positive" : ""}>
                  {item.points >= 0 ? "+" : ""}{item.points} pts
                </strong>
              )}
            </div>
            <p>{item.description}</p>
            <time dateTime={item.occurredAt}>{item.displayDate}</time>
          </div>
        </article>
      ))}
    </div>
  );
}

function HomePage({ snapshot }: { snapshot: AppSnapshot }) {
  const { member, coupons, activity, news } = snapshot;

  return (
    <main id="main-content" className="page-stack home-page">
      <section className="welcome-row" aria-labelledby="welcome-title">
        <div>
          <p className="eyebrow">Buenos días</p>
          <h1 id="welcome-title">Hola, {member.name}</h1>
        </div>
        <Link className="icon-button" to="/activity" aria-label="Ver notificaciones y actividad">
          <Icon name="bell" size={22} />
          <span className="notification-dot" aria-hidden="true" />
        </Link>
      </section>

      <section className="balance-card" aria-label="Resumen de fidelización">
        <div className="balance-card__glow" aria-hidden="true" />
        <div className="balance-card__heading">
          <div>
            <span className="balance-card__label">Tu saldo</span>
            <p className="balance-card__points">{formatPoints(member.points)} <small>pts</small></p>
          </div>
          <span className="level-badge"><Icon name="sparkles" size={15} /> {member.level}</span>
        </div>
        <div className="progress-block">
          <div className="progress-block__labels">
            <span>{member.progress}% hacia {member.nextLevel}</span>
            <span>{formatPoints(member.pointsToNextLevel)} pts restantes</span>
          </div>
          <div className="progress-track" role="progressbar" aria-valuenow={member.progress} aria-valuemin={0} aria-valuemax={100} aria-label={`Progreso hacia ${member.nextLevel}`}>
            <span style={{ width: `${member.progress}%` }} />
          </div>
        </div>
        <Link className="balance-card__action" to="/profile">
          Ver mi cuenta <Icon name="arrow" size={18} />
        </Link>
      </section>

      <section aria-labelledby="quick-title">
        <h2 className="sr-only" id="quick-title">Accesos rápidos</h2>
        <div className="quick-actions">
          <Link to="/benefits"><span><Icon name="ticket" size={23} /></span>Mis cupones</Link>
          <Link to="/activity"><span><Icon name="activity" size={23} /></span>Actividad</Link>
          <Link to="/profile"><span><Icon name="user" size={23} /></span>Mi perfil</Link>
        </div>
      </section>

      <section aria-labelledby="benefits-title">
        <SectionHeading eyebrow="Para ti" title="Beneficios destacados" linkTo="/benefits" />
        <div className="coupon-grid" id="benefits-title">
          {coupons.slice(0, 2).map((coupon, index) => (
            <CouponCard coupon={coupon} featured={index === 0} key={coupon.id} />
          ))}
        </div>
      </section>

      <section className="story-card" aria-labelledby="story-title">
        <div className="story-card__art" aria-hidden="true">
          <span><Icon name="sparkles" size={34} /></span>
        </div>
        <div className="story-card__content">
          <p className="eyebrow">{news[0]?.category}</p>
          <h2 id="story-title">{news[0]?.title}</h2>
          <p>{news[0]?.summary}</p>
          <Link className="secondary-action" to="/benefits">Descubrir más</Link>
        </div>
      </section>

      <section aria-labelledby="activity-title">
        <SectionHeading title="Actividad reciente" linkTo="/activity" />
        <div id="activity-title"><ActivityList items={activity.slice(0, 2)} compact /></div>
      </section>
    </main>
  );
}

function BenefitsPage({ coupons }: { coupons: Coupon[] }) {
  return (
    <main id="main-content" className="page-stack">
      <header className="page-header">
        <p className="eyebrow">Tu selección</p>
        <h1>Beneficios</h1>
        <p>Ventajas disponibles para disfrutar ahora y propuestas seleccionadas para ti.</p>
      </header>
      <div className="filter-row" aria-label="Filtros de beneficios">
        <span className="filter-chip filter-chip--active">Todos</span>
        <span className="filter-chip">Disponibles</span>
        <span className="filter-chip">Próximamente</span>
      </div>
      <section aria-labelledby="coupon-list-title">
        <SectionHeading title={`${coupons.length} beneficios disponibles`} />
        <h2 className="sr-only" id="coupon-list-title">Listado de beneficios</h2>
        {coupons.length > 0 ? (
          <div className="coupon-grid coupon-grid--catalog">
            {coupons.map((coupon, index) => <CouponCard coupon={coupon} featured={index === 0} key={coupon.id} />)}
          </div>
        ) : (
          <FeedbackState icon="ticket" title="No hay beneficios disponibles" description="Vuelve pronto para descubrir nuevas ventajas." />
        )}
      </section>
    </main>
  );
}

function ActivityPage({ activity }: { activity: ActivityItem[] }) {
  return (
    <main id="main-content" className="page-stack">
      <header className="page-header">
        <p className="eyebrow">Todo al día</p>
        <h1>Actividad</h1>
        <p>Consulta tus puntos, beneficios y últimas interacciones.</p>
      </header>
      <section aria-labelledby="activity-list-title">
        <h2 className="section-title" id="activity-list-title">Últimos movimientos</h2>
        <ActivityList items={activity} />
      </section>
    </main>
  );
}

function ProfilePage({ member }: { member: AppSnapshot["member"] }) {
  return (
    <main id="main-content" className="page-stack">
      <header className="profile-header">
        <span className="profile-avatar profile-avatar--large" aria-hidden="true">{member.initials}</span>
        <div>
          <p className="eyebrow">Mi perfil</p>
          <h1>{member.fullName}</h1>
          <p>Miembro desde {member.memberSince}</p>
        </div>
      </header>

      <section className="membership-card" aria-labelledby="membership-title">
        <div>
          <span className="membership-card__label">Nivel actual</span>
          <h2 id="membership-title">{member.level}</h2>
        </div>
        <Icon name="sparkles" size={28} />
        <p><strong>{formatPoints(member.points)} puntos</strong> disponibles para tus próximas ventajas.</p>
      </section>

      <section aria-labelledby="account-title">
        <h2 className="section-title" id="account-title">Tu cuenta</h2>
        <div className="settings-list">
          <div><span><Icon name="user" size={20} /></span><div><strong>Datos personales</strong><small>Nombre, idioma y preferencias</small></div></div>
          <div><span><Icon name="bell" size={20} /></span><div><strong>Comunicaciones</strong><small>Noticias y notificaciones</small></div></div>
          <Link to="/showcase"><span><Icon name="phone" size={20} /></span><div><strong>Vista iPhone</strong><small>Modo de presentación comercial</small></div><Icon name="chevron" size={18} /></Link>
          <Link to="/system"><span><Icon name="settings" size={20} /></span><div><strong>Estado de la demo</strong><small>Información técnica y capacidades</small></div><Icon name="chevron" size={18} /></Link>
        </div>
      </section>
    </main>
  );
}

function IPhoneShowcase() {
  return (
    <main className="showcase-page">
      <header className="showcase-toolbar">
        <div>
          <p className="eyebrow">Modo de presentación</p>
          <h1>Convercus App en iPhone</h1>
        </div>
        <Link className="showcase-close" to="/">
          <Icon name="close" size={19} />
          <span>Salir</span>
        </Link>
      </header>

      <section className="iphone-stage" aria-label="Simulación visual de Convercus App en un iPhone">
        <div className="iphone-device">
          <span className="iphone-device__speaker" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--action" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--volume-up" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--volume-down" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--power" aria-hidden="true" />
          <iframe
            className="iphone-device__screen"
            src="/"
            title="Convercus App — vista iPhone"
          />
          <span className="iphone-device__home-indicator" aria-hidden="true" />
        </div>
      </section>

      <p className="showcase-note">
        Simulación visual a 393 × 852 px. La validación en un iPhone real se realizará en A5.
      </p>
    </main>
  );
}

function SystemPage() {
  const isOnline = navigator.onLine;

  return (
    <main id="main-content" className="page-stack">
      <header className="page-header page-header--internal">
        <p className="eyebrow">Panel interno</p>
        <h1>Estado de la demo</h1>
        <p>Información para preparar y verificar la demostración.</p>
      </header>
      <section className="system-panel" aria-label="Estado del sistema">
        <dl className="system-list">
          <div><dt>Marca</dt><dd>{brand.name}</dd></div>
          <div><dt>Datos</dt><dd><span className="technical-badge">{appConfig.dataMode}</span></dd></div>
          <div><dt>Red</dt><dd>{isOnline ? "disponible" : "sin conexión"}</dd></div>
          <div><dt>Baseline</dt><dd>{appConfig.tesBaseline}</dd></div>
          <div><dt>Futura</dt><dd>bloqueada hasta verificar licencia</dd></div>
        </dl>
      </section>
      <Link className="back-link" to="/profile"><Icon name="arrowBack" size={18} /> Volver al perfil</Link>
    </main>
  );
}

const navigation: { to: string; label: string; icon: IconName }[] = [
  { to: "/", label: "Inicio", icon: "home" },
  { to: "/benefits", label: "Beneficios", icon: "ticket" },
  { to: "/activity", label: "Actividad", icon: "activity" },
  { to: "/profile", label: "Perfil", icon: "user" },
];

function AppShell({ snapshot }: { snapshot: AppSnapshot }) {
  return (
    <div className="app-shell">
      <a className="skip-link" href="#main-content">Saltar al contenido</a>
      <header className="topbar">
        <Link to="/" aria-label="Ir al inicio">
          <img className="brand-logo" src={brandAssets.logoPrimaryUrl} alt="Convercus" />
        </Link>
        <Link className="profile-avatar" to="/profile" aria-label="Abrir perfil">
          {snapshot.member.initials}
        </Link>
      </header>

      <Routes>
        <Route path="/" element={<HomePage snapshot={snapshot} />} />
        <Route path="/benefits" element={<BenefitsPage coupons={snapshot.coupons} />} />
        <Route path="/activity" element={<ActivityPage activity={snapshot.activity} />} />
        <Route path="/profile" element={<ProfilePage member={snapshot.member} />} />
        <Route path="/system" element={<SystemPage />} />
        <Route path="*" element={<FeedbackState icon="compass" title="Esta página no existe" description="Vuelve al inicio para seguir explorando." action={{ label: "Ir al inicio", to: "/" }} />} />
      </Routes>

      <nav className="bottom-nav" aria-label="Navegación principal">
        {navigation.map(({ to, label, icon }) => (
          <NavLink to={to} end={to === "/"} key={to}>
            <Icon name={icon} size={22} />
            <span>{label}</span>
          </NavLink>
        ))}
      </nav>
    </div>
  );
}

export function App() {
  const location = useLocation();
  const [snapshot, setSnapshot] = useState<AppSnapshot>();
  const [error, setError] = useState(false);

  useEffect(() => {
    adapter.getSnapshot().then(setSnapshot).catch(() => setError(true));
  }, []);

  if (location.pathname === "/showcase") {
    return <IPhoneShowcase />;
  }

  if (error) {
    return <FeedbackState icon="warning" title="No hemos podido cargar la App" description="Comprueba la conexión e inténtalo de nuevo." action={{ label: "Reintentar", onClick: () => window.location.reload() }} />;
  }

  if (!snapshot) {
    return <FeedbackState loading title="Preparando tu espacio" description="Estamos cargando tus beneficios." />;
  }

  return <AppShell snapshot={snapshot} />;
}
