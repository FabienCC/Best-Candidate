from typing import List, NamedTuple
from copy import deepcopy

Piece = NamedTuple('Piece', [('x', float), ('y', float), ('z', float)])

DESC = lambda x: -x

def get_pieces_for(objective_piece: Piece, library: List[Piece]) -> List[Piece]:
    # pieces contains the currently selected pieces, library_left the remaining pieces to choose from
    pieces, library_left = [], deepcopy(library)

    # Iterate until we can fill the entire Y axis
    while sum(piece.y for piece in pieces) < objective_piece.y:
        try:
            best_next_piece = sorted(
                filter(
                    # Filter out pieces which are too thin, or too narrow
                    lambda piece: piece.z >= objective_piece.z and piece.x >= objective_piece.x,
                    library_left,
                ),
                # Get largest piece in Y as possible
                key=lambda piece: DESC(piece.y),
            )[0]
        except IndexError:
            raise Exception(
                'No suitable pieces in library: current_pieces={0}, library={1}, curren_length={2}'.format(
                    pieces,
                    library,
                    sum(piece.y for piece in pieces),
                ),
            )

        # Add next best piece to selected pieces
        pieces.append(best_next_piece)

        # Remove best_next_piece from available pieces
        library_left.remove(best_next_piece)

        # Make sure no pieces get lost in the process
        assert len(pieces) + len(library_left) == len(library), (len(pieces), len(library_left), len(library))

    # Simply return the pieces in the order they were selected
    return pieces

if __name__ == '__main__':
    OBJECT_DIMENSION = Piece(10, 10, 10) # (X, Y, Z)

    LIBRARY = [
        Piece(10, 1, 10),
    ] * 10

    print(get_pieces_for(OBJECT_DIMENSION, LIBRARY))
