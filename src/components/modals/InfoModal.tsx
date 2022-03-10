import { Cell } from '../grid/Cell'
import { BaseModal } from './BaseModal'

type Props = {
  isOpen: boolean
  handleClose: () => void
}

export const InfoModal = ({ isOpen, handleClose }: Props) => {
  return (
    <BaseModal title="How to play" isOpen={isOpen} handleClose={handleClose}>
      <p className="text-sm text-gray-500 dark:text-gray-300">
        Wordle but for human proteins!
        Guess their UniProt IDs! </p>
      <p> Get suggestion on <a href="https://www.uniprot.org/uniprot/?query=taxonomy%3A9606&sort=score">Uniprot</a></p>
        <p>
        (a crude copy of <a href="https://geneofthe.day">geneofthe.day</a>)

      </p>
    </BaseModal>
  )
}
