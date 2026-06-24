import { useState, useEffect } from "react";
import { User, Building2, Briefcase, Globe, X, Plus, Loader2, Trash2 } from "lucide-react";
import { api } from "../api.js";

const TYPE_ICONS = {
  PERSON: User,
  BANK: Building2,
  AGENCY: Briefcase,
  COMPANY: Globe,
  OTHER: User,
};

const TYPE_LABELS = {
  PERSON: "Person",
  BANK: "Bank",
  AGENCY: "Agency",
  COMPANY: "Company",
  OTHER: "Other",
};

export default function EntitiesPanel({ evidenceId, onLinked }) {
  const [entities, setEntities] = useState([]);
  const [linked, setLinked] = useState([]);
  const [showCreate, setShowCreate] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState(null);
  const [query, setQuery] = useState("");

  const [newEntity, setNewEntity] = useState({ name: "", type: "OTHER", description: "" });

  const refresh = async () => {
    try {
      const [all, linkedToEvidence] = await Promise.all([
        api.listEntities(query),
        api.evidenceEntities(evidenceId),
      ]);
      setEntities(all);
      setLinked(linkedToEvidence);
      setError(null);
    } catch (e) {
      setError(e.message);
    }
  };

  useEffect(() => {
    refresh();
  }, [evidenceId, query]);

  async function create() {
    if (!newEntity.name.trim()) return;
    setBusy(true);
    setError(null);
    try {
      const created = await api.createEntity(newEntity);
      setNewEntity({ name: "", type: "OTHER", description: "" });
      setShowCreate(false);
      await refresh();
    } catch (e) {
      setError(e.message);
    } finally {
      setBusy(false);
    }
  }

  async function link(entityId, role = null) {
    setBusy(true);
    try {
      await api.linkEvidence(entityId, evidenceId, role);
      await refresh();
      onLinked?.();
    } catch (e) {
      setError(e.message);
    } finally {
      setBusy(false);
    }
  }

  async function unlink(entityId) {
    setBusy(true);
    try {
      await api.unlinkEvidence(entityId, evidenceId);
      await refresh();
      onLinked?.();
    } catch (e) {
      setError(e.message);
    } finally {
      setBusy(false);
    }
  }

  async function deleteEntity(id) {
    if (!confirm("Delete this entity?")) return;
    setBusy(true);
    try {
      await api.deleteEntity(id);
      await refresh();
    } catch (e) {
      setError(e.message);
    } finally {
      setBusy(false);
    }
  }

  const linkedIds = new Set(linked.map((e) => e.id));

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-semibold text-zinc-200">Linked entities</h3>
        <button
          onClick={() => setShowCreate(true)}
          className="flex items-center gap-1 rounded bg-zinc-800 px-2 py-1 text-xs text-zinc-300 hover:bg-zinc-700"
        >
          <Plus size={12} /> New entity
        </button>
      </div>

      {linked.length === 0 ? (
        <p className="text-xs text-zinc-600">No entities linked yet.</p>
      ) : (
        <div className="space-y-2">
          {linked.map((e) => {
            const Icon = TYPE_ICONS[e.type] || User;
            return (
              <div
                key={e.id}
                className="flex items-center justify-between rounded-lg border border-zinc-800 bg-zinc-900/50 px-3 py-2"
              >
                <div className="flex items-center gap-2">
                  <Icon size={14} className="text-zinc-500" />
                  <div>
                    <div className="text-sm font-medium text-zinc-200">{e.name}</div>
                    <div className="text-xs text-zinc-600">
                      {TYPE_LABELS[e.type]}
                      {e.role && ` · ${e.role}`}
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => unlink(e.id)}
                  className="text-zinc-600 hover:text-red-400"
                  title="Unlink"
                >
                  <X size={14} />
                </button>
              </div>
            );
          })}
        </div>
      )}

      {showCreate && (
        <div className="rounded-lg border border-zinc-800 bg-zinc-900 p-3">
          <div className="mb-3 flex items-center justify-between">
            <span className="text-xs font-medium text-zinc-300">Create entity</span>
            <button onClick={() => setShowCreate(false)} className="text-zinc-600 hover:text-zinc-300">
              <X size={14} />
            </button>
          </div>
          <div className="space-y-2">
            <input
              value={newEntity.name}
              onChange={(e) => setNewEntity({ ...newEntity, name: e.target.value })}
              placeholder="Name"
              className="w-full rounded border border-zinc-700 bg-zinc-950 px-2 py-1.5 text-sm text-zinc-100 outline-none focus:border-emerald-500"
            />
            <select
              value={newEntity.type}
              onChange={(e) => setNewEntity({ ...newEntity, type: e.target.value })}
              className="w-full rounded border border-zinc-700 bg-zinc-950 px-2 py-1.5 text-sm text-zinc-100 outline-none focus:border-emerald-500"
            >
              {Object.entries(TYPE_LABELS).map(([val, label]) => (
                <option key={val} value={val}>
                  {label}
                </option>
              ))}
            </select>
            <input
              value={newEntity.description}
              onChange={(e) => setNewEntity({ ...newEntity, description: e.target.value })}
              placeholder="Description (optional)"
              className="w-full rounded border border-zinc-700 bg-zinc-950 px-2 py-1.5 text-sm text-zinc-100 outline-none focus:border-emerald-500"
            />
            <button
              onClick={create}
              disabled={busy || !newEntity.name.trim()}
              className="w-full rounded bg-emerald-600 py-1.5 text-xs font-medium text-white hover:bg-emerald-500 disabled:opacity-50"
            >
              {busy ? <Loader2 size={12} className="inline animate-spin" /> : "Create & link"}
            </button>
          </div>
        </div>
      )}

      <div className="relative">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search to link existing entity…"
          className="w-full rounded border border-zinc-700 bg-zinc-900 px-3 py-2 text-sm text-zinc-100 outline-none focus:border-emerald-500"
        />
      </div>

      {query && entities.length > 0 && (
        <div className="max-h-48 space-y-1 overflow-y-auto rounded-lg border border-zinc-800 bg-zinc-900 p-2">
          {entities.map((e) => {
            const Icon = TYPE_ICONS[e.type] || User;
            const isLinked = linkedIds.has(e.id);
            return (
              <div
                key={e.id}
                className="flex items-center justify-between rounded px-2 py-1.5 hover:bg-zinc-800"
              >
                <div className="flex items-center gap-2">
                  <Icon size={12} className="text-zinc-500" />
                  <span className="text-sm text-zinc-200">{e.name}</span>
                  <span className="text-xs text-zinc-600">{TYPE_LABELS[e.type]}</span>
                </div>
                {isLinked ? (
                  <span className="text-xs text-zinc-600">Linked</span>
                ) : (
                  <button
                    onClick={() => link(e.id)}
                    className="text-xs text-emerald-400 hover:text-emerald-300"
                  >
                    Link
                  </button>
                )}
              </div>
            );
          })}
        </div>
      )}

      {error && <p className="text-xs text-red-400">{error}</p>}
    </div>
  );
}
