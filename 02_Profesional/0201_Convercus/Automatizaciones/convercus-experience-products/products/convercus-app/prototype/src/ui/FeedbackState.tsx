import { Link } from "react-router-dom";
import { Icon, type IconName } from "./Icon";

interface FeedbackAction {
  label: string;
  to?: string;
  onClick?: () => void;
}

export function FeedbackState({
  icon = "compass",
  title,
  description,
  action,
  loading = false,
}: {
  icon?: IconName;
  title: string;
  description: string;
  action?: FeedbackAction;
  loading?: boolean;
}) {
  return (
    <main id="main-content" className="feedback-state" aria-live="polite" aria-busy={loading}>
      <span className={`feedback-state__icon${loading ? " feedback-state__icon--loading" : ""}`}>
        {loading ? <span className="spinner" aria-hidden="true" /> : <Icon name={icon} size={30} />}
      </span>
      <h1>{title}</h1>
      <p>{description}</p>
      {action?.to && <Link className="primary-action" to={action.to}>{action.label}</Link>}
      {action?.onClick && <button className="primary-action" type="button" onClick={action.onClick}>{action.label}</button>}
    </main>
  );
}
