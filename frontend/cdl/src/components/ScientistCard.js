import './styles/ScientistCard.css';

function ScientistCard({ name, image }) {
  return (
    <div className="scientist-logo text-center">
      <img src={image} alt={name} className="scientist-img" />
      <div className="scientist-name">{name}</div>
    </div>
  );
}

export default ScientistCard;
